"""
    abs()  求绝对值
    round()  四舍五入
"""
print(abs(-10))  # 10
print(round(1.2))  # 1
print(round(1.9))  # 2

"""
    高阶函数
    简化代码，提高灵活性
"""


def sum_num(a, b, f):
    return f(a) + f(b)


print(sum_num(1.1, 2.7, abs))
print(sum_num(1.1, 2.7, round))

"""
    内置高阶函数
    map  (函数名，序列名)
    reduce （函数名，序列名） reduce() 传入的参数func 必须接收两个参数
                           前一次的结果和序列的下一个元素做累积计算
    filter (函数名，序列名)    过滤掉不符合条件的元素，返回一个filter对象。
                            若要转换为list，list()
"""

list1 = [i for i in range(5)]


def func(x):
    return x ** 2


result = map(func, list1)
print(result)  # <map object at 0x7fc3edc3c340>
print(list(result))  # [0, 1, 4, 9, 16]

import functools

result = functools.reduce(lambda a, b: a + b, list1)
print(result)  # 10

result = filter(lambda x: x % 2 == 0, list1)
print(list(result))  # [0, 2, 4]
