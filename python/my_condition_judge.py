"""
使用魔法
"""
# ------------------------------------------------------------------------
# 条件与循环简化
# expression1 if condition else expression2 for item in iterable
# expression for item in iterable if condition

# [(xx, yy) for xx in x for yy in y if xx != yy]

s = {1, 2, 3}
s1 = s.copy()
s1.remove(1)
print(s1)
print(s)
