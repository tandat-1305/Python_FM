# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:36:56 2020

@author: Administrator
"""
print("Sinh ngẫu nhiên 1 dictionary")
import string,random
dic=dict()
n_ten=random.randrange(2,6)
rd=random.choice(string.ascii_uppercase)
name=rd+''.join(random.choice(string.ascii_lowercase) for i in range(n_ten-1)) 
dic['name']=name
age=random.randrange(1,100)
dic['age']=age
print("Dictionary: ",dic)