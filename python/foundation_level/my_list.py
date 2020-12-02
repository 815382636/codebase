"""
    一、list
    函数index （查找元素)
    函数index （查找元素，开始坐标)
    函数index （查找元素，开始坐标，结束坐标 + 1）

"""
namelist = ['tom', 'lily', 'rose']
print(namelist.index('rose'))
print(namelist.index('rose', 0))
print(namelist.index('rose', 0, 3))

# count
print(namelist.count('tom'))

"""
    len()
    in
    not in
    append
    insert(index, value)
"""

"""
    extend
    序列拆开 --逐一追加到list
"""
namelist.extend('xiaoming')
print(namelist)  # ['tom', 'lily', 'rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
namelist.extend([1, 2, 3])
print(namelist)  # ['tom', 'lily', 'rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g', 1, 2, 3]

"""
    删除操作
    del 目标  del namelist    del namelist[0]
    pop(index) 删除指定下标的数据，默认删除最后一个数据，并返回数据
    remove(value)
    clear() 清空
"""

"""
    .reverse()  逆序
    .sort()     排序  默认升序
"""
namelist = namelist[:3]
namelist.sort()
print(namelist)
namelist.sort(reverse=True)
print(namelist)

"""
    .copy()  复制
"""

"""
    如何以就地操作方式打乱一个列表的元素？
"""
import random

l = [1, 2, 4, 5]
random.shuffle(l)
print(l)
