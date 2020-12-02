import os

"""
    1. 如何读写文本文件？
"""
print('-----1. 如何读写文本文件？-----')

s = '你好'
s1 = s.encode('utf-8')
print(s1)
with open('1.txt', 'wt', encoding='utf8') as f:
    f.write(s)

with open('1.txt', 'rt', encoding='utf8') as f:
    t = f.read()
    print(t)

os.remove('1.txt')

"""
    2. 如何设置文件的缓冲？
"""
print('\n\n\n-----2. 如何设置文件的缓冲？------')

f = open('1.txt', 'w', buffering=2048)  # 全缓冲
# f = open('1.txt', 'w', buffering=1)  # 行缓冲
# f = open('1.txt', 'w', buffering=0)  # 无缓冲
f.write('abc')
f.write('+' * 4093)
f.write('-')
f.close()
# os.remove('1.txt')

"""
    3. 如何访问文件的状态？
"""
import stat
import time

print('\n\n\n-----3. 如何访问文件的状态？-----')
print(os.stat(
    '1.txt'))  # os.stat_result(st_mode=33188, st_ino=60989444, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=4097, st_atime=1606889963, st_mtime=1606889963, st_ctime=1606889963)

print(os.lstat('1.txt'))

s = os.stat('1.txt')
print(s.st_mode)
# print(help(stat))

t = s.st_atime
print(time.localtime(t))

print(os.path.isdir('1.txt'))
print(os.path.isfile('1.txt'))
print(os.path.islink('1.txt'))

"""
    4. 如何使用临时文件？
"""
print('\n\n\n-----4. 如何使用临时文件？-----')
from tempfile import TemporaryFile, NamedTemporaryFile

f = TemporaryFile(mode='w')
f.write('abcdef' * 100000)
f.seek(0)
# print(f.read())

ntf = NamedTemporaryFile()
print(ntf.name)

os.remove('1.txt')