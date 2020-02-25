import cv2
import numpy as np
img = cv2.imread("/Users/yuyang/Downloads/liuyifei.jpg")

h, w, _ = img.shape

new_img = img[0:h//2, 0:w//2]

cv2.imwrite("/Users/yuyang/Downloads/liuyifei_caijian.jpg", new_img)


