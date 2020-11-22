# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:50:15 2020

@author: Administrator
"""
#bai 1
print("Bài 1")
print("Có thể chuyển câu lệnh lặp không xác định bằng vòng lặp While sang vòng lặp For ")
x = ['1','2','3','4','5','6','7']
for x in range(1,8,3):
         print(x)

#bai 2 
print("Bài 2")
print("Giai phuong trinh bac nhat ")
a = int(input("a= "))
b = int(input("b= "))
if a == 0 :
    if b == 0 :
        print("phuong trinh VSN")
    else:
        print("phuong trinh VN")
else:
    print("phuong trinh co nghiem x= :",-b/a)

#bai 3
print("Bài 3")
print('''Cú pháp: for a in b :
         Khối lệnh của for
Ý nghĩa mỗi thành phần: a là chuỗi cần lặp, b là biến nhận giá trị của từng mục bên trong chuoi_lap trên mỗi lần lặp. 
Vòng lặp sẽ tiếp tục cho đến khi nó lặp tới mục cuối cùng trong chuỗi.
''')
chuoi = ['hồng','lan','mai']
for tu in chuoi:
    print('hoa',tu)   

#bai 5
print("Bài 5")
nhap_list1 = input("nhập phần tử list bằng space: ")
list1 = nhap_list1.split()
print("List la: ", list1)
sum = 0
for num in list1:
    sum += int(num)
print("Sum = ", sum)

#bai 6 va 7
print("Bài 6 & 7")
import random
n = int(input("nhập số phần tử: "))    
randomlist = random.sample(range(1, 30),n)
print("Ramdomlist",randomlist)
max=randomlist[0]
min=randomlist[0]
for i in randomlist:
    if i>max:
        max=i
for i in randomlist:
    if i<min:
        min=i
print("GTLN: ",max)
print("GTNN: ",min)



            
        
    
    

