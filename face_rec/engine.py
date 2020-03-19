#coding: utf-8
import numpy as np
import cv2
import os

def load(img_file):
    img = cv2.imread(img_file)
    retImg = cv2.resize(img, (36,20))
    retImg = cv2.cvtColor(retImg, cv2.COLOR_RGB2GRAY)
    retImg = cv2.equalizeHist(retImg)
    # cv2.imshow('img', retImg)
    # cv2.waitKey(5000)
    return retImg

def createImgMat(img_dir):
    index = 0
    label = []
    for f in os.listdir(img_dir):
        f_path = os.path.join(img_dir, f)
        img = load(f_path)
        tempImg = np.reshape(img, (-1, 1))
        if index == 0:
            dataMat = tempImg
        else:
            dataMat = np.column_stack((dataMat, tempImg))
        label.append(f_path)
        index += 1
    return dataMat, label

def pca(dataMat, dimNum):
    rows,cols = dataMat.shape
    data_mean = np.mean(dataMat, 0)
    A = dataMat - np.tile(data_mean, (rows, 1))
    A = np.mat(A)
    C = A * A.T
    D, V = np.linalg.eig(C)
    V_r = V[:, 0:dimNum]
    V_r = A.T * V_r
    for i in range(dimNum):
        V_r[:,1] = V_r[:,i]/np.linalg.norm(V_r[:,i])

    final_data = A * V_r
    return final_data, data_mean, V_r

def compare(img_path, V):
    img = load(img_path)
    tempImg = np.reshape(img, (-1, 1))
    # 归一化
    tempImg = tempImg / float(np.linalg.norm(tempImg))
    print(np.linalg.norm(tempImg))
    ret = V.T * np.mat(tempImg)
    print(ret)
    pass


if __name__ == '__main__':
    retMat, label = createImgMat('/Users/yuyang/Downloads/face')
    ret, data_mean, v_r = pca(retMat, 40)
    print(ret.shape)
    print(v_r.shape)
    print(np.linalg.norm(v_r, axis=0))
    compare('/Users/yuyang/Downloads/dog2.jpeg', ret)



