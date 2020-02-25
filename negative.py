#coding: utf-8
"""
图像负片
"""

import cv2
import numpy as np

img = cv2.imread("/Users/yuyang/Downloads/liuyifei.jpg")

if img is None:
    raise 'file open error'

height = img.shape[0]
width = img.shape[1]

negative_file = np.zeros((height, width, 3))

b, g, r = cv2.split(img)

r = 255 - r
b = 255 - b
g = 255 - g

negative_file[:,:,0] = b
negative_file[:,:,1] = g
negative_file[:,:,2] = r

cv2.imwrite("/Users/yuyang/Downloads/negative_liuyifei.jpg", negative_file)


