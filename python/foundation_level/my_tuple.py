t1 = (10, 20, 30)
t2 = (10,)  # 定义单个数据的元组 切记加个,
t3 = (10)
t4 = ("123")
print(type(t2))
print(type(t3))
print(type(t4))

"""
    index()
    len()
    tup[xxx]
"""


"""
    tuple 修改
"""
t5 = ('aa', 'bb', ['cc', 'dd'])
print(t5)
t5[2][0] = 'ee'
print(t5)
