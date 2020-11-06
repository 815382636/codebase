"""
    除法向上取整
"""
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
