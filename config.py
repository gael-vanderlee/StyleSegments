from pathlib import Path

# Folders and file paths
project_path = Path(__file__).parent.resolve()

input_folder = project_path / "input/"
input_folder.mkdir(parents=True, exist_ok=True)
images_folder = input_folder / "images/"
images_folder.mkdir(parents=True, exist_ok=True)
styles_folder = input_folder / "styles"
styles_folder.mkdir(parents=True, exist_ok=True)

output_folder = project_path / "output/"
output_folder.mkdir(parents=True, exist_ok=True)
segmentation_folder = output_folder / "segmentations/"
segmentation_folder.mkdir(parents=True, exist_ok=True)
stylized_folder = output_folder / "stylized/"
stylized_folder.mkdir(parents=True, exist_ok=True)
combined_folder = output_folder / "combined/"
combined_folder.mkdir(parents=True, exist_ok=True)

overwrite = False
mask_blur_size = 100

# Images to process for this run
images = ["ville.png"]

ims_config = {
    "cat.jpg": {
        "seg_models": ["VOC"],
        "styles": ["cartoon.jpg"],
        "class": [0]   # One per style
    },
    "ville.png": {
        "seg_models": ["VOC", "ADE20k", "Cityscapes"],
        "styles": ["cartoon.jpg"],
        "class": [8]   # One per model
    }
}

images_paths = [images_folder / image for image in images]
for im_path in images_paths:
    assert im_path.exists(), f"{im_path} doesn't exist"
    assert im_path.name in ims_config, f"Please choose a config for {im_path.name}"
