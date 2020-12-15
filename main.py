from config import images_paths, ims_config, combined_folder, overwrite, mask_blur_size
from segmentation.segment_image import transfer_styles
from style_transfer.style_transfer import StyleTransferModel
import cv2
import numpy as np
from pathlib import Path

if __name__ == "__main__":

    # Get all the masks
    masks = {}
    for im_path in images_paths:
        masks[im_path] = {}
        for seg_model in ims_config[im_path.name]["seg_models"]:
            masks[im_path][seg_model] = transfer_styles(im_path, seg_model)

    # Get all the styles
    style_model = StyleTransferModel(images_paths, ims_config, overwrite=overwrite)
    styles = style_model.run()

    # Combine the two
    for im_path in images_paths:
        for i, seg_model in enumerate(ims_config[im_path.name]["seg_models"]):
            for style in ims_config[im_path.name]["styles"]:

                # Get the data for this image, style and model
                seg_class = ims_config[im_path.name]["class"][i]
                mask = masks[im_path][seg_model].astype("uint8")
                stylized = styles[im_path][style]

                # Apply mask and get final image
                original = cv2.imread(im_path.as_posix())
                original = cv2.resize(original, stylized.shape[:2][::-1])
                mask = cv2.resize(mask, stylized.shape[:2][::-1])
                mask = (mask == seg_class).astype("uint8")
                mask = cv2.blur(mask * 255, (mask_blur_size, mask_blur_size)) / 255
                mask = np.expand_dims(mask, 2)
                mask = np.repeat(mask, 3, axis=2)
                output = (original.astype(float) * (1 - mask) + stylized.astype(float) * mask).astype("uint8")
                impath = combined_folder / (im_path.stem + "_" + seg_model + "_" + Path(style).stem + ".jpeg")
                cv2.imwrite(impath.as_posix(), output)
                print(f"\n***** DONE *****\nSaved final image to {impath}")

                # Show outputs
                cv2.imshow("Original image", original)
                cv2.imshow("Stylized image", stylized)
                cv2.imshow("Final image", output)
                cv2.waitKey()
