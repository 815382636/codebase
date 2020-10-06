from functools import reduce

"""
使用魔法
"""


# --------------------------------------------------------------------
# global MIN_VALUE  函数修改全局变量需声明
# nonlocal x        内部函数修改外部函数需声明

# --------------------------------------------------------------------
# 闭包example


def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是exponent_of函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方

print(square(2))  # 计算2的平方
print(cube(2))  # 计算2的立方

# --------------------------------------------------------------------
# lambda example
print([(lambda x: x * x)(x) for x in range(10)])

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1])  # 按列表中元组的第二个元素排序
print(l)

# --------------------------------------------------------------------
# 函数式编程 example

l = [1, 2, 3, 4, 5]
new_list = map(lambda x: x * 2, l)  # [2， 4， 6， 8， 10]
new_list1 = filter(lambda x: x % 2 == 0, l)  # [2, 4]
new_list2 = reduce(lambda x, y: x * y, l)  # 1*2*3*4*5 = 120
