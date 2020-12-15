"""
    原型模式
"""

import copy
from collections import OrderedDict


class Book:
    def __init__(self, name, authors, price, **rest):
        """
        rest的例子有：出版商、长度、标签、出版日期
        """
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)  # 添加其他额外属性

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


class Prototype:
    def __init__(self):
        self.objects = dict()  # 初始化一个原型列表

    def register(self, identifier, obj):
        # 在原型列表中注册原型对象
        self.objects[identifier] = obj

    def unregister(self, identifier):
        # 从原型列表中删除原型对象
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        # 根据 identifier 在原型列表中查找原型对象并克隆
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)  # 用新的属性值替换原型对象中的对应属性
        return obj


def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'),
              price=118, publisher='Prentice Hall', length=228, publication_date='1978-02-22',
              tags=('C', 'programming', 'algorithms', 'data structures'))

    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99, length=274,
                         publication_date='1988-04-01', edition=2)

    for i in (b1, b2):
        print(i)
    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))


if __name__ == '__main__':
    main()
