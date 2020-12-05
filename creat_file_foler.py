# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:45:40 2020

@author: Administrator
"""

#13.2
import os
print("Nhập tên thư mục: ")
foldername = input()
print("Nhập tên file: ")
filename = input() + ".txt  "
os.chdir('C:\Test')
os.mkdir(foldername)
a = open(filename, 'w') 



         