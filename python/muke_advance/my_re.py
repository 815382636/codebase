import re

#   前面+r ,代表原字符串，里面有\n不转义
pa = re.compile(r'imooc')
str1 = 'imooc  safd'
ma = pa.match(str1)
print(ma)  # <re.Match object; span=(0, 5), match='imooc'>
print(ma.group())  # imooc
print(ma.span())  # (0, 5)

pa = re.compile(r'imooc', re.I)  # 匹配大小写
str1 = 'ImoOc  safd'
ma = pa.match(str1)
print(ma)
print(ma.group())  # ImoOc
print(ma.span())

pa = re.compile(r'(imooc)', re.I)
ma = pa.match(str1)
print(ma.groups())  # ('ImoOc',)

ma = re.match(r'ImoOc', str1)
print(ma.group())

"""
    .               匹配任意字符(除了\n)
    [...]           匹配字符集
    \d/\D           匹配数字/非数字
    \s/\S           匹配空白/非空白字符
    \w/\w           匹配单词字符[a-zA-Z0-9]/非单词字符   
    *               匹配前一个字符0次或者无限次
    +               匹配前一个字符1次或者无限次
    ?               匹配前一个字符0次或者1次
    {m}/{m,n}       匹配前一个字符m次或者n次
    *? /+? /??      匹配模式变成非贪婪(尽可能少匹配字符)
    ^               匹配字符串开头
    $               匹配字符串结尾
    \A/\Z           指定的字符串必须出现在开头结尾
    |               匹配左右任意一个表达式                 r'abc|d'
    (ab)            括号中表达式作为一个分组                r'^[\w]{4,10}@(163|126).com$', 'imooc@163.com'
    \<number>       引用编号为num的分组匹配到的字符串        r'<([\w]+>)[\w]+</\1', '<book>python</book>'
    (?P<name>)      分组起一个别名                        r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>python</book>'
    (?P=name)       引用别名为name的分组匹配字符串
"""

ma = re.match(r'.', 'b')
print(ma)
print(ma.group())
print(re.match(r'{.}', '{0}').group())
print(re.match(r'{[abc]}', '{a}').group())
print(re.match(r'{[a-z]}', '{d}').group())

print(re.match(r'{[a-zA-Z0-9]}', '{d}').group())
print(re.match(r'{[\w]}', '{d}').group())  # \w/\w           匹配单词字符[a-zA-Z0-9]/非单词字符
print(re.match(r'{[\W]}', '{ }').group())
print(re.match(r'\[[\w]\]', '[a]').group())
print(re.match(r'[A-Z][a-z]*', 'Aadgsagasg').group())
print(re.match(r'[_a-zA-Z]+[_\w]*', '_Aadgsagasg').group())
print(re.match(r'[1-9]?[0-9]', '99').group())
print(re.match(r'[A-Z]{3,8}', 'ABCDEF').group())
print(re.match(r'^[\w]{4,10}@163.com$', 'imooc@163.com').group())

"""
    1. search
    2. findall
    3. sub
    4. split
"""

str1 = 'imooc videonum = 1000'
print(re.search(r'\d+', str1).group())  # 1000

str2 = 'c++=100, java=90, python=80'
print(re.findall(r'\d+', str2))  # ['100', '90', '80']

st3 = 'imooc videonum = 1000'
print(re.sub(r'\d+', '1001', st3))  # imooc videonum = 1001
print(re.sub(r'\d+', lambda x: str(int(x.group()) + 1), st3))  # imooc videonum = 1001

str4 = 'imooc:C C++ Java|Python, C#'
print(re.split(r':|,| |\|', str4))
