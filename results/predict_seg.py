from keras_segmentation.pretrained import pspnet_50_ADE_20K , pspnet_101_cityscapes, pspnet_101_voc12

model1 = pspnet_50_ADE_20K() # load the pretrained model trained on ADE20k dataset

model2 = pspnet_101_cityscapes() # load the pretrained model trained on Cityscapes dataset

model3 = pspnet_101_voc12() # load the pretrained model trained on Pascal VOC 2012 dataset

# load any of the 3 pretrained models
inp = "chicago.jpg"
n = "chicago"

out = model1.predict_segmentation(
    inp=inp,
    out_fname=n+"1.png"
)

out = model2.predict_segmentation(
    inp=inp,
    out_fname=n+"2.png"
)

out = model3.predict_segmentation(
    inp=inp,
    out_fname=n+"3.png"
)

print("finished")
