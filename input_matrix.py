# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:13:51 2020

@author: Administrator
"""
a = int(input("Số hàng: " ))
b = int(input("Số cột : "))
matran=[]
i=1
j=1
for i in range(a):
    c=[]
    for j in range(b):
        j=int(input("Nhập số : hàng "+str(i+1)+" cột "+str(j+1)+":"" "))
        c.append(j)
    print() 
    matran.append(c)
for i in range(a):
    for j in range(b):
        print(matran[i] [j],end =" ")
    print() 
    