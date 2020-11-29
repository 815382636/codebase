"""
    引用
    id()        判断两个变量是否为同一个值的引用
"""
a = 1
b = 1
print(id(a))
print(id(b))

l1 = [1, 2, 3]
l2 = l1.copy()
print(id(l1))
print(id(l2))

"""
    可变类型：
        list
        dict
        set
    不可变类型：
        int
        float
        str
        tuple
"""
