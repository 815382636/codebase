"""
    1. 如何在列表，字典，集合中根据条件筛选数据
"""
import random
import timeit
from functools import reduce

print("-----1. 如何在列表，字典，集合中根据条件筛选数据-----")
l = [random.randint(-10, 10) for _ in range(10)]
print(l)

#   1. 使用filter函数
print(list(filter(lambda x: x >= 0, l)))
#   2. 使用列表解析  ---速度更快
print([x for x in l if x >= 0])

d = {i: random.randint(0, 100) for i in range(10)}
print(d)
print({k: v for k, v in d.items() if v >= 90})

s = set(l)
print({i for i in s if i % 3 == 0})

"""
    2. 如何为元组中的每个元素命名，提高程序可读性
        (1) 定义常量
"""
print("\n\n\n-----2. 如何为元组中的每个元素命名，提高程序可读性-----")
NAME, AGE, SEX, EMAIL = 0, 1, 2, 3
l = ['小明', 18, '男', '111dfsfe@163.com']
print(f'姓名：{l[NAME]}，年龄：{l[AGE]}，性别：{l[SEX]}，邮箱：{l[EMAIL]}，')  # 姓名：小明，年龄：18，性别：男，邮箱：111dfsfe@163.com，

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('小明', 18, '男', '111dfsfe@163.com')
print(s.name, s.age, s.sex, s.email)
# namedtuple 是 tuple 的子类
print(isinstance(s, tuple))  # True
print(tuple(s))

"""
    3. 如何统计序列中元素的出现频度
"""
print("\n\n\n-----3. 如何统计序列中元素的出现频度-----")
l = [random.randint(0, 10) for _ in range(30)]
print(l)  # [1, 8, 8, 3, 3, 8, 7, 7, 8, 6, 9, 5, 8, 5, 4, 8, 1, 5, 9, 7, 1, 5, 1, 0, 9, 3, 2, 7, 2, 7]
from collections import Counter

c = Counter(l)
print(c.most_common(3))  # [(8, 6), (7, 5), (1, 4)]

"""
    4. 如何根据字典中值的大小，对字典中的项进行排序
"""
print('\n\n\n-----4. 如何根据字典中值的大小，对字典中的项进行排序-----')
d = {i: random.randint(60, 100) for i in range(10)}
print(d)  # {0: 66, 1: 85, 2: 92, 3: 61, 4: 72, 5: 77, 6: 91, 7: 87, 8: 73, 9: 71}
print(sorted(d.items(), key=lambda x: x[1]))  # [3, 0, 9, 4, 8, 5, 1, 7, 6, 2]

l = list(zip(d.values(), d.keys()))
print(sorted(l))

"""
    5. 如何快速找到多个字典中的公共键(key)
"""
print('\n\n\n-----5. 如何快速找到多个字典中的公共键(key)-----')

s1 = {x: random.randint(1, 4) for x in random.sample('abstreg', random.randint(3, 6))}
print(s1)
s2 = {x: random.randint(1, 4) for x in random.sample('abstreg', random.randint(3, 6))}
print(s2)
s3 = {x: random.randint(1, 4) for x in random.sample('abstreg', random.randint(3, 6))}
print(s3)

print([k for k in s1 if k in s2 and k in s3])
print(s1.keys() & s2.keys() & s3.keys())

print(map(lambda x: x.keys(), [s1, s2, s3]))
print(reduce(lambda a, b: a & b, map(lambda x: x.keys(), [s1, s2, s3])))

"""
    6. 如何让字典保持有序
"""
print('\n\n\n-----6. 如何让字典保持有序-----')
from collections import OrderedDict

d = OrderedDict()
d['Jim'] = 30
d['Tom'] = 35
d['army'] = 40
print(d)

"""
    7. 如何实现用户的历史记录功能(最多n条) 双端循环队列
"""
print('\n\n\n-----7. 如何实现用户的历史记录功能(最多n条)-----')
from collections import deque
import pickle
import os

d = deque([], 3)
for i in range(10):
    d.append(random.randint(1, 10))
    print(d)
pickle.dump(d, open('1.txt', 'wb'))   # 写二进制文件， pickle.dump 后成byte
p = pickle.load(open('1.txt', 'rb'))
print(f'p:{p}')
os.remove('1.txt')
