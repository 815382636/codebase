# 将一个字符串中的内容转换成python原来的格式
st1 = '1'
st2 = '1.1'
st3 = '[1,2,3]'
st4 = '(1,2,3)'
print(eval(st1))
print(eval(st2))
print(eval(st3))
print(eval(st4))
print(type(eval(st1)))
print(type(eval(st2)))
print(type(eval(st3)))
print(type(eval(st4)))

# 整数转unicode
print(chr(97))
# unicode转整数
print(ord('a'))
# 十进制转16进制
print(hex(16))
# 十进制转2进制
print(bin(16))
# 十进制转8进制
print(oct(16))
# 2，8，16进制转10进制
print(int('1010', 2))
print(int('0o72', 8))
print(int('0x72', 16))
