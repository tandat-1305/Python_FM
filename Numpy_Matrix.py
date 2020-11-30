# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:32:34 2020

@author: Administrator
"""
#Numpy
import numpy as np
a = np.array([[1, 2],
             [3, 4]])
b = np.array([[10, 20,],
              [40, 50,]])
c = np.array([[2,4,6],[1,3,5]])
print("Tổng hai ma trận: ")
print(a+b)
print("Tích a và b: ")
print(a.dot(b))
print("Ma trận chuyển vị: ")
print(np.transpose(c))
