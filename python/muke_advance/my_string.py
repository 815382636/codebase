"""
    1. 如何拆分含有多种分隔符的字符串？
"""
print('-----1. 如何拆分含有多种分隔符的字符串？-----')
s = 'ew,f|l\tjj;we;ov\tk;erw;er|v,f'


# print(s.split())  # split 方法不传参默认用空格


def mySplit(s, ds):
    res = [s]
    for i in ds:
        t = []
        # map返回的是迭代器，迭代器是惰性加载，不遍历不计算，自然看不到输出
        # map(lambda x: t.extend(x.split(i)), res)    # 直接使用不生效
        list(map(lambda x: t.extend(x.split(i)), res))
        res = t
    return [i for i in res if i]


print(mySplit(s, ',;\t|'))

import re

# re.split 传入的第一个参数为正则表达式
print(re.split('[,;\t|]+', s))

"""
    2. 如何判断字符串a是否以字符串b开头或结尾?
    s.startswith()
    s.endswith()
"""
print('\n\n\n-----2. 如何判断字符串a是否以字符串b开头或结尾?-----')
# endwith 传参可以使用元组
print(s.endswith((';er|v,f', ',f')))

"""
    3. 如何调整字符串中文本的格式？
"""
print('\n\n\n-----3. 如何调整字符串中文本的格式？-----')

s = ['2016-05-23', '2016-05-23', '2016-05-23', '2016-05-23', '2016-05-24']
print([re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', i) for i in s])
print([re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', i) for i in s])

"""
    4. 如何将多个小字符串拼接成一个大字符串？
        (1) +       对应于 __add__()函数
        (2) ''.join(st1, st2)
"""
print('\n\n\n-----4. 如何将多个小字符串拼接成一个大字符串？-----')

"""
    5. 如何对字符串进行左，右，居中对齐？
"""
print('\n\n\n-----5. 如何对字符串进行左，右，居中对齐？-----')

s = 'abc'
print(s.ljust(20))  # (abc                 )
print(s.rjust(20))  # (                 abc)
print(s.center(20))  # (        abc         )
print(s.ljust(20, '-'))  # (abc-----------------)
print(format(s, '<20'))  # (abc                 )
print(format(s, '>20'))  # (                 abc)
print(format(s, '^20'))  # (        abc         )

"""
    6. 如何去掉字符串中不需要的字符？
"""
print('\n\n\n-----6. 如何去掉字符串中不需要的字符？-----')
s = '     abc   123     '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
s = '----abc+++++'
print(s.strip('+-'))  # 删除+-
print(s.replace('-', ''))  # 只能替换一种
print(re.sub('[+-]', '', s))


