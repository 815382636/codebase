"""
    主访问模式：
    r 只读
    w 写
    a 追加
    其他：
    rb
    wb
    ab      带b的为2进制操作
    r+
    w+      带+都是可读可写
    rb+
    wb+     2进制可读可写
"""

"""
    read()
    read(num)  读取数据的长度，单位字节
    readlines() 全部读取，返回一个list，list中每一个元素是每一行
    readline()  读取一行内容，多次调用，对象的指针会下移
    文件读取要确保文件大小的问题
        with open('1,txt', 'r') as fin:
        while True:
            s = fin.read(1024)
            while not s:
                break
            print(s)
"""

# with open('1.txt', 'r') as fin:
#     l = fin.readlines()

"""
    seek(偏移量， 起始位置) 0开头 1当前 2结尾
"""

# with open('1.txt', 'r') as fin:
#     fin.seek(2, 0)  # 从文件第二个元素开始读取
#     fin.seek(0, 2)  # 将文件指针放到文件结尾

"""
    文件与文件夹操作
    os.rename(目标文件名，新文件名)
    os.remove(目标文件名)
    
    文件夹操作
    os.mkdir(文件夹名字)     创建文件夹
    os.rmdir(文件夹名字)     删除文件夹
    os.getcwd()            获取当前目录
    os.chdir(目录)          改变默认目录 change dir
    os.listdir()           查看当前目录下所有文件
"""
import os

with open('1.txt', 'w') as fin:
    fin.write("123")
os.remove('1.txt')
