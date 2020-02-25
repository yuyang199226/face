import cv2
import numpy as np

img = cv2.imread("/Users/yuyang/Downloads/liuyifei.jpg")

if img is None:
    raise "open file failed"

print(img.shape)

new_img = cv2.resize(img, (40,40), interpolation=cv2.INTER_AREA)

cv2.imwrite('/Users/yuyang/Downloads/liuyifei_small.jpg', new_img)

print(new_img.shape)

new_img2 = cv2.resize(img, None, fx=0.5, fy=0.6, interpolation=cv2.INTER_AREA)

print(new_img2.shape)

cv2.imwrite('/Users/yuyang/Downloads/liuyifei_small2.jpg', new_img2)


