# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:47:41 2020

@author: Administrator
"""

import random,string
dic_list=list()
#Random số ptử
n=random.randrange(50,101)
print("Số phần tử là: ",n)
#In list dictionary
i=1
for i in range(n):
    dic=dict()
    n_ten=random.randrange(2,6)
    rd=random.choice(string.ascii_uppercase)
    name=rd+''.join(random.choice(string.ascii_lowercase) for i in range(n_ten-1)) 
    dic['name']=name
    age=random.randrange(1,100)
    dic['age']=age
    dic_list.append(dic)
print("List là:",dic_list)