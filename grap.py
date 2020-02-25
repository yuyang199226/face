import numpy as np
import cv2


img = cv2.imread("/Users/yuyang/Downloads/liuyifei.jpg")
if img is None:
    raise "img not found"
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(gray_img.shape)

cv2.imwrite("/Users/yuyang/Downloads/liuyifei_gray.jpg", gray_img)

