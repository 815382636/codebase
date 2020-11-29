"""
    创建set可以使用{}和set(),但空集合创建只能用set()
    set有去重
"""

"""
    增  
    add()
    update()
"""
s1 = {10, 20}
s1.update([30, 40])
s1.update('121321')
print(s1)

"""
    删除
    remove() 删除指定数据，数据不存在则报错
    discard() 
    pop()  一般不使，随机删除元素
"""
s1.remove(10)
s1.discard(20)
s1.discard(20)
print(s1)
