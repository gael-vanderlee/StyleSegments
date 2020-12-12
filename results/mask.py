import cv2
import numpy as np
import os

""" ça va changer selon les librairies a voir si on automatise """
tree_l = np.array([1, 1, 1])
tree_h = np.array([207, 132, 300])
sky_l = np.array([150, 150, 150])
sky_h = np.array([207, 300, 300])
building_l = np.array([100, 100, 200])
building_h = np.array([220, 250, 250])


""" files """
input_path = "test.png"
name = os.path.splitext(input_path)[0]

""" style on scpecific area """
frame = cv2.imread(input_path)
seg = cv2.imread(name+"1.png")
style = cv2.imread(name+"_stylized.png")

mask = cv2.inRange(seg, sky_l, sky_h)
overlay = cv2.bitwise_and(style, style, mask= mask)
background = cv2.bitwise_and(frame, frame, mask= 255-mask)

res = overlay+background

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('overlay', overlay)
cv2.imshow('background', background)
cv2.imshow('res', res)
cv2.imwrite('chicago_res1.png', res)

cv2.imwrite(name+'_res.png', res)

cv2.waitKey()
