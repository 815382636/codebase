"""
    创建
    dic1 = {}
    dic2 = dict()
"""

"""
    删除操作
    del     del dict[key]
    clear()
"""

"""
    dict.get(key)
    dict.keys()
    dict.values()
    for i, v in dict.items():
"""

dict1 = {i: i ** 2 for i in range(5)}
print(dict1)

list1 = ['name', 'age', 'gender']
list2 = ['xiaoming', '18', 'man']
# dict1 = {list1[i]: list2[i] for i in range(len(list1))}
dict1 = dict(zip(list1, list2))
print(dict1)

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']
          ]

list1 = [dict(zip(attributes, value)) for value in values]
print(list1)
