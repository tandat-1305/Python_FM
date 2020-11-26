# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:48:21 2020

@author: Administrator
"""
list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}), 
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}), 
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}), 
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for i,j in list2:
    print(i)
    for a,b in enumerate(i,start=1):
        print("Vị trí " ,a, ":" ,i.get(b))
    print(j)    
    for c,d in enumerate(j,start=1):
        print("Vị trí " ,c, ":" ,j.get(d))    
              
 
