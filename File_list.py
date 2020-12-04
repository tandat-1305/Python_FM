# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:31:39 2020

@author: Administrator
"""
#13.1.2
import os
base = r'C:'
lst = os.listdir(base)
print("Dữ liệu ổ C: ",lst)
print("")
#13.1.3
list1 = []
list2 = []
for i in os.listdir(base):
    if os.path.isfile(os.path.join(base, i)):
        list1.append(i)
    if os.path.isdir(os.path.join(base, i)):
        list2.append(i)
print("Các tập tin: ", list1)  
print("")      
print("Các thư mục: ", list2)