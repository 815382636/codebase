"""
    help函数作用：查看函数的说明文档
"""
help(len)


def my_sum(a, b):
    """
    求和函数
    :param a: 参数1
    :param b: 参数2
    :return: 返回参数1和参数2之和
    """
    return a + b


print(my_sum(1, 2))
print(help(my_sum))  # 返回""""""中的内容

"""
    dir()函数的作用
    Dir()函数也是Python内置函数，dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
    带参数时，返回参数的属性、方法列表。
"""
print(dir(
    str.join))  # ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__le__', '__lt__', '__name__', '__ne__',
# '__new__', '__objclass__', '__qualname__', '__reduce__', '__reduce_ex__', '_
# _repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']

"""
    函数修改全局变量    先 global 一下
    内函数修改外函数的值  先 nonlocal 一下
"""
a = 100


def modify():
    global a
    a = 200


modify()
print(a)

"""
    函数 return 多个值时，默认使用tuple保存 
"""

"""
    函数传参
    1. 按位置传参
    2. 按参数传参 (id = 10,name = 'xiaoming')
    3. 缺省参数传参，尽量使用参数传参
    4. 不定长参数
    5. 包裹关键字传递
                        4,5统称为一个组包的过程
    6. 返回值 return 多个值       用多个变量接收即为拆包的过程（一个变量接收到的位tuple）
"""


def user_info(*args):
    print(args)


user_info("1")  # ('1',)
user_info("1", "nihao", "xiaoming")  # ('1', 'nihao', 'xiaoming')


def user_info_n(**kwargs):
    print(kwargs)


user_info_n(name='Tom', age=18, id=110)
