"""
    lambda  匿名函数
    简化代码，节省开销
    lambda 参数列表 ： 表达式
"""
f1 = lambda: 100
print(f1())

f2 = lambda a, b: a + b
print(f2(1, 2))
print((lambda a, b: a + b)(1, 2))

f3 = lambda a, b, c=100: a + b + c
print(f3(1, 2))

f4 = lambda *args: sum(args)
print(f4(1, 2, 3, 4))

students = [{'age': 11}, {'age': 20}, {'age': 18}]
students.sort(key=lambda x: x['age'])
print(students)
