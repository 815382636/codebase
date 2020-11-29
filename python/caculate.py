"""
    除法向上取整
"""
import itertools

a = 12
b = 5
print(-(-a // b))
print((a + b - 1) // b)

"""
    bin()函数，返回传参的2进制形式，type是str
"""
a = 10
print(bin(a))
print(bin(a).count('1'))

"""
    正无穷，负无穷的使用
"""
a = float('inf')
b = float('-inf')
c = 0x3f3f3f3f
d = -0x3f3f3f3f
print(a, b, c, d)

"""
    bisect 库
    https://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html
"""
import bisect

s = [1, 2, 4]
print(bisect.bisect_left(s, 1), bisect.bisect_right(s, 1))

"""
    ASCII码 与字符的相互转换

"""
b = 97
print(chr(b))
print(ord('a'))
print(ord('A'))
print(ord('1'))

"""
    python itertools 高效combinations
"""
print(list(itertools.combinations(range(1, 5), 2)))

"""
    random
"""
import random

for i in range(10):
    print(random.randint(0, 2), end="\t")
