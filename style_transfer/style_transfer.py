from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.optim as optim
from torchvision import transforms, models
from config import styles_folder, ims_config, stylized_folder
from pathlib import Path
from tqdm import trange


class StyleTransferModel:

    def __init__(self, images_paths, im_styles, show_images=True):
        self.model = models.vgg19(pretrained=True).features

        for param in self.model.parameters():
            param.requires_grad_(False)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.images_paths = images_paths
        self.im_styles = im_styles
        self.show_images = show_images
        self.style_weights = {'conv1_1': 1.,
                              'conv2_1': 0.8,
                              'conv3_1': 0.5,
                              'conv4_1': 0.3,
                              'conv5_1': 0.1}

        self.content_weight = 1  # alpha
        self.style_weight = 1e6  # beta

        self.show_every = 400
        self.steps = 4000  # decide how many iterations to update your image (5000)
        self.max_size = 800

    def load_image(self, img_path, shape=None):
        """ Load in and transform an image, making sure the image
           is <= 400 pixels in the x-y dims."""

        image = Image.open(img_path).convert('RGB')

        # large images will slow down processing
        if max(image.size) > self.max_size:
            size = self.max_size
        else:
            size = max(image.size)

        if shape is not None:
            size = shape

        in_transform = transforms.Compose([
            transforms.Resize(size),
            transforms.ToTensor(),
            transforms.Normalize((0.485, 0.456, 0.406),
                                 (0.229, 0.224, 0.225))])

        # discard the transparent, alpha channel (that's the :3) and add the batch dimension
        image = in_transform(image)[:3, :, :].unsqueeze(0)

        return image

    def im_convert(self, tensor):
        """ Display a tensor as an image. """

        image = tensor.to("cpu").clone().detach()
        image = image.numpy().squeeze()
        image = image.transpose(1, 2, 0)
        image = image * np.array((0.229, 0.224, 0.225)) + np.array((0.485, 0.456, 0.406))
        image = image.clip(0, 1)

        return image

    def get_features(self, image, layers=None):
        """ Run an image forward through a model and get the features for
            a set of layers. Default layers are for VGGNet matching Gatys et al (2016)
        """

        # Need the layers for the content and style representations of an image
        if layers is None:
            layers = {'0': 'conv1_1',
                      '5': 'conv2_1',
                      '10': 'conv3_1',
                      '19': 'conv4_1',
                      '28': 'conv5_1',
                      '21': 'conv4_2'}

        features = {}
        x = image
        for name, layer in self.model._modules.items():
            x = layer(x)
            if name in layers:
                features[layers[name]] = x

        return features

    def gram_matrix(self, tensor):
        """ Calculate the Gram Matrix of a given tensor
            Gram Matrix: https://en.wikipedia.org/wiki/Gramian_matrix
        """

        # get the batch_size, depth, height, and width of the Tensor
        _, d, h, w = tensor.size()
        # reshape it, so we're multiplying the features for each channel
        tensor = tensor.view(d, h * w)
        # calculate the gram matrix
        gram = torch.mm(tensor, tensor.t())

        return gram

    def train(self, target, optimizer, content_features, style_grams):
        for ii in trange(1, self.steps + 1, desc="Training the StyleTransfer Model"):

            # Calculate the content loss
            target_features = self.get_features(target)
            content_loss = torch.mean(
                (target_features['conv4_2'] - content_features['conv4_2']) ** 2)

            # Style loss
            # initialize the style loss to 0
            style_loss = 0
            # iterate through each style layer and add to the style loss
            for layer in self.style_weights:
                # get the "target" style representation for the layer
                target_feature = target_features[layer]
                _, d, h, w = target_feature.shape

                target_gram = self.gram_matrix(target_feature)

                style_gram = style_grams[layer]
                layer_style_loss = self.style_weights[layer] * torch.mean((target_gram - style_gram) ** 2)

                # add to the style loss
                style_loss += layer_style_loss / (d * h * w)

            total_loss = content_loss * self.content_weight + style_loss * self.style_weight

            # update your target image
            optimizer.zero_grad()
            total_loss.backward()
            optimizer.step()

            # display intermediate images and print the loss
            if ii % self.show_every == 0:
                print('Total loss: ', total_loss.item())
                if self.show_images:
                    plt.imshow(self.im_convert(target))
                    plt.show()

    def run(self):
        output = {}

        for image_path in self.images_paths:
            output[image_path] = {}
            for style_name in self.im_styles[image_path.name]["styles"]:
                content = self.load_image(image_path.as_posix()).to(self.device)
                style = self.load_image((styles_folder / style_name).as_posix(), shape=content.shape[-2:]).to(self.device)

                if self.show_images:
                    # Display the images
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
                    # Content and style ims side-by-side
                    ax1.imshow(self.im_convert(content))
                    ax2.imshow(self.im_convert(style))

                # Get content and style features only once before forming the target image
                content_features = self.get_features(content)
                style_features = self.get_features(style)

                # Calculate the gram matrices for each layer of our style representation
                style_grams = {layer: self.gram_matrix(style_features[layer]) for layer in style_features}
                target = content.clone().requires_grad_(True).to(self.device)
                optimizer = optim.Adam([target], lr=0.003)

                self.train(target, optimizer, content_features, style_grams)

                if self.show_images:
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
                    ax1.imshow(self.im_convert(content))
                    ax2.imshow(self.im_convert(target))

                # Save the output
                out_path = stylized_folder / (image_path.stem + "_" + Path(style_name).stem + ".png")
                out_image = (self.im_convert(target) * 255).astype(np.uint8)
                im = Image.fromarray(out_image)
                im.save(out_path.as_posix())
                print(f"Saved image at {out_path}")
                output[image_path][style_name] = out_image

        return output


if __name__ == "__main__":
    model = StyleTransferModel([Path('../input/images/cat.jpg')], ims_config)
    model.run()
