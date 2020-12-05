import os
os.chdir('C:\Test')
dulieu = input("Nhập dữ liệu: ")
fileName = input("Nhập tên file: ") + '.txt'
f = open(fileName, 'w')
f.write(dulieu)
f.close()
os.startfile(fileName)