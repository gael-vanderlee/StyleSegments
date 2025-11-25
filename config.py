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
mask_blur_size = 10

# Images to process for this run
images = ["building.jpg", "cat.jpg"]

ims_config = {
    "cat.jpg": {
        "seg_models": ["VOC"],  # ["ADE20k", "Cityscapes", "VOC", "resnet_VOC"]
        "styles": ["cartoon.jpg", "mondrian.jpg", "van_gogh.jpg"],
        "class": [8]   # One per model
    },
    "ville.png": {
        "seg_models": ["ADE20k"],
        "styles": ["mondrian.jpg"],
        "class": [1]   # One per model
    },
    "chicago.jpg": {
        "seg_models": ["ADE20k"],
        "styles": ["mondrian.jpg"],
        "class": [2]  # One per model
    },
    "building.jpg": {
        "seg_models": ["ADE20k"],
        "styles": ["van_gogh.jpg"],
        "class": [1]  # One per model
    }
}

images_paths = [images_folder / image for image in images]
for im_path in images_paths:
    assert im_path.exists(), f"{im_path} doesn't exist"
    assert im_path.name in ims_config, f"Please choose a config for {im_path.name}"
