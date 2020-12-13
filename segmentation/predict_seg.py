from keras_segmentation.pretrained import pspnet_50_ADE_20K , pspnet_101_cityscapes, pspnet_101_voc12
from config import images_folder, segmentation_folder

model1 = pspnet_50_ADE_20K() # load the pretrained model trained on ADE20k dataset

model2 = pspnet_101_cityscapes() # load the pretrained model trained on Cityscapes dataset

model3 = pspnet_101_voc12() # load the pretrained model trained on Pascal VOC 2012 dataset

# load any of the 3 pretrained models
image = images_folder / "me.jpg"
assert image.exists()

out = model1.predict_segmentation(
    inp=image.as_posix(),
    out_fname=(segmentation_folder / (image.stem + "_1.png")).as_posix()
)

out = model2.predict_segmentation(
    inp=image.as_posix(),
    out_fname=(segmentation_folder / (image.stem + "_2.png")).as_posix()
)

out = model3.predict_segmentation(
    inp=image.as_posix(),
    out_fname=(segmentation_folder / (image.stem + "_3.png")).as_posix()
)

print("finished")
