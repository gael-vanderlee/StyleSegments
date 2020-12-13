from segmentation.keras_segmentation.pretrained import *
from config import segmentation_folder


def transfer_styles(image_path, model_name):
    assert image_path.exists(), f"{image_path} does not exist"
    out_path = (segmentation_folder / (image_path.stem + "_" + model_name + ".png")).as_posix()

    if model_name == "ADE20k":
        model = pspnet_50_ADE_20K()
    elif model_name == "Cityscapes":
        model = pspnet_101_cityscapes()
    elif model_name == "VOC":
        model = pspnet_101_voc12()
    else:
        raise ValueError(f"You chose {model_name} but available models are ADE20k, Cityscapes and VOC")

    print(f"Running segmentation for {image_path} with {model_name}")
    out = model.predict_segmentation(
        inp=image_path.as_posix(),
        out_fname=out_path
    )
    print(f"Finished, results saved at {out_path}")

    return out
