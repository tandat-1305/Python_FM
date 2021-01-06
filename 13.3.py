import os, random, string, math
def get_size(start_path = '.'):
    tong_size_thumuc = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for i in filenames:
            fp = os.path.join(dirpath, i)
            tong_size_thumuc += os.path.getsize(fp)
    return tong_size_thumuc
def randomstring(length):
    ki_tu = string.ascii_lowercase + string.ascii_uppercase + '0123456789'
    return ''.join(random.choice(ki_tu) for i in range(length))
foldername = str(input('Nhập tên thư mục: '))
filename = str(input('Nhập tên tệp tin: '))
size = 1048576 * float(input('Nhập dung lượng dữ liệu giới hạn là 1MB <= size <= 1024MB: '))
os.mkdir('C:\%s' %foldername)
os.chdir('C:\%s' %foldername)
for i in range(int(size/1048576)+1):
    if float(get_size('C:\%s' %foldername)) <= size-1024*1000:
        f = open(filename+'%d' %i,'a')
        f.write(randomstring(1024*1000))
        f.close()
    else:
        f = open(filename+'%d' %i,'a')
        f.write(randomstring(int(size)-get_size('C:\%s' %foldername)))
        f.close()