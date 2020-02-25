import cv2
import numpy as np

img = cv2.imread("/Users/yuyang/Downloads/liuyifei.jpg")

h, w, _ = img.shape

rotate_img = cv2.getRotationMatrix2D((w/2, h/2), 45, 1)
cv2.imwrite('xxx.jpg', rotate_img)
