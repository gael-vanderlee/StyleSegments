from config import images_paths, ims_config, combined_folder
from segmentation.segment_image import transfer_styles
from style_transfer.style_transfer import StyleTransferModel
import cv2
import numpy as np
from pathlib import Path

if __name__ == "__main__":
    # TODO don't run if file exists

    # Get all the masks
    masks = {}
    for im_path in images_paths:
        masks[im_path] = {}
        for seg_model in ims_config[im_path.name]["seg_models"]:
            masks[im_path][seg_model] = transfer_styles(im_path, seg_model)

    # Get all the styles
    style_model = StyleTransferModel(images_paths, ims_config)
    styles = style_model.run()

    # Combine the two
    for im_path in images_paths:
        for seg_model in ims_config[im_path.name]["seg_models"]:
            for i, style in enumerate(ims_config[im_path.name]["styles"]):
                # Get the data for this image, style and model
                seg_class = ims_config[im_path.name]["class"][i]
                mask = masks[im_path][seg_model].astype("uint8")
                stylized = styles[im_path][style]

                # Apply mask and get final image
                original = cv2.imread(im_path.as_posix())
                output = cv2.resize(original, stylized.shape[:2][::-1])
                mask = cv2.resize(mask, stylized.shape[:2][::-1])
                mask = mask == seg_class
                mask = np.expand_dims(mask, 2)
                mask = np.repeat(mask, 3, axis=2)
                output[mask] = stylized[mask]
                impath = combined_folder / (im_path.stem + "_" + seg_model + "_" + Path(style).stem + ".jpeg")
                cv2.imwrite(impath.as_posix(), output)
                print(f"Saved final image to {impath}")

                # Show outputs
                cv2.imshow("Original image", original)
                cv2.imshow("Mask image", mask)
                cv2.imshow("Stylized image", stylized)
                cv2.imshow("Final image", output)

