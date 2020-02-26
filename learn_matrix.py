#coding: utf-8
import numpy as np

#初始化一个matrix
a = np.matrix([[0,1,0],
    [1,0,0],
    [0,0,1]
    ])
# 逆
c = np.linalg.inv(a)
print(c)

# matrix 的逆
print("a 的 转置")
print(a.T)
# matrix 的转置 transpose

b = np.transpose(a)
print("a 的转置")
print(b)

# matrix 乘法
print("乘法")
print(a * b)

