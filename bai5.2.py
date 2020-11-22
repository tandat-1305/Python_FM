# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:24:45 2020

@author: Administrator
"""

import numpy as np
n = int(input("Giá trị phần tử = "))
lt = np.random.random_sample(size = n)*20000-10000
n = 1
print ("List =",lt)
import math
for x in lt:
    print ("Giá trị phần tử thứ ",n,"=",x)
    n=n+1
    if x > 0:
         print ("Logarith của phần tử thứ",n,"=",math.log(x))
    else:
        print ("Không có Logarith")