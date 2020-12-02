"""
    1. 如何读写csv数据？
"""
import os
import csv

print('-----1. 如何读写csv数据？-----')
with open('movie.csv', 'r') as rf:
    reader = csv.reader(rf)
    for l in reader:
        s = l
        break

with open('movie.csv', 'w') as wf:
    writer = csv.writer(wf)
    writer.writerow(s)

os.remove('movie.csv')

"""
    2. 如何读写json数据？
"""
import json

l = [1, 2, 'abc', {'name': 'Bob', 'age': 13}]
print(json.dumps(l))
print(json.dumps(l, separators=[',', ':']))
# loads

"""
    3. 如何解析简单的xml文档？
"""
from xml.etree.ElementTree import parse

print('\n\n\n-----3. 如何解析简单的xml文档？-----')

f = open('demo.xml')
et = parse(f)
print(et)
root = et.getroot()
print(1, root)
print(2, root.tag)
print(3, root.attrib)
print(4, root.text)
# 1 <Element '{http://www.w3.org/2000/svg}svg' at 0x7ff2af3b72c0>
# 2 {http://www.w3.org/2000/svg}svg
# 3 {'width': '66', 'height': '73', 'viewBox': '0 0 66 73'}
# 4 None

print(root.iter())
