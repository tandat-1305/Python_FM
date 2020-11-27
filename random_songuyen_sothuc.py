# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 20:30:50 2020

@author: Administrator
"""

import random
n = random.randrange(50,1000)
print("số phần tử là :",n)
a=random.sample(range(-1000,1000),n)
b=[random.uniform(-1000.0,1000.0) for i in range(n)]
print("List số nguyên: ",a)
print("List số thực  : ",b)      