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
