"""

    while 条件：
        条件成立重复执行的代码
    else:
        循环正常结束之后要执行的代码

"""

#  非正常退出和正常退出
#  break 执行了 else 下方的代码不执行
# continue 执行了 else 下方的代码执行
print('-------while--------')
n = 5
while n:
    n -= 1
    if n == 2:
        break
    print(n)
else:
    print("正常结束")

n = 5
while n:
    n -= 1
    print(n)
else:
    print("正常结束")

print('-------for--------')
for i in range(5):
    print(i)
else:
    print('正常结束')
