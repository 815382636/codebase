stu_id = 1
weight = 1.1
print("我的学号是：%d" % stu_id)
print("我的学号是：%03d" % stu_id)
print("我的学号是：%03d, 体重是：%.2f" % (stu_id, weight))
print("我的学号是：%03d, 体重是：%.2f".format(stu_id, weight))

"""
        f''
"""
print(f'我的学号是：{stu_id}, 体重是: {weight}')
print(f"体重是： {weight:.2f}")
print(f"学号是： {stu_id:03d}")
print(f"{{ {10 * 8} }}")

name = 'abc'
print(f'name={name.upper()}')

dict1 = {'name': 'qer', 'age': 123}
print(f'名字：{dict1.get("name")},年龄：{dict1.get(str("age"))}')

"""
        f-string 函数与匿名函数输出
"""


def sum(a, b):
    return a + b


print(f'2+3={sum(2, 3)}')
print(f'x+y的和为：{(lambda x, y: x + y)(2, 3)}')

"""
        f-string 秘密语法
"""
name = 'a'
age = '18'
print(f'{name=},{age=}')
