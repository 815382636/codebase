"""
    1. 如何实现可迭代对象和迭代器对象？
"""
print('-----1. 如何实现可迭代对象和迭代器对象？-----')
l = [i for i in range(5)]  # l 称为可迭代对象
l_it = iter(l)  # l_it 称为迭代器对象
print(l_it.__next__())  # 0
print(l_it.__next__())  # 1

from collections.abc import Iterable, Iterator
import random


class WeatherIterator(Iterator):  # 迭代器对象，需要实现next()方法
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def city_weather(self, city):
        return {city: random.randint(-10, 10)}

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.city_weather(city)


class WeatherIterable(Iterable):  # 可迭代对象，需要实现 __iter__ 方法

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


print([i for i in WeatherIterable(['Shandong', 'Zhejiang', 'Chongqing'])])

"""
    2. 如何使用生成器函数实现可迭代对象？
        -   实现一个可迭代对象的类，它能迭代出给定范围内的所有素数
    ******************************迭代对象next()函数别忘加终止条件*****************************************
"""
print('\n\n\n-----2. 如何使用生成器函数实现可迭代对象？\n------   实现一个可迭代对象的类，它能迭代出给定范围内的所有素数-----')


class PrimeNumbersIterator(Iterator):

    def __init__(self, start, end):
        self.start, self.end = start, end

    # 判断质数
    @staticmethod
    def isPrime(n):
        if n <= 3:
            return n > 1
        if n % 6 != 1 and n % 6 != 5:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        while not PrimeNumbersIterator.isPrime(self.start) and self.start <= self.end:
            self.start += 1
        k = self.start
        self.start += 1
        return k


class PrimeNumbers(Iterable):

    def __init__(self, start, end):
        self.start, self.end = start, end

    def __iter__(self):
        # 通过生成器函数实现可迭代对象
        for i in range(self.start, self.end + 1):
            if PrimeNumbersIterator.isPrime(i):
                yield i

        # 通过迭代器实现可迭代对象
        # return PrimeNumbersIterator(self.start, self.end)


print([i for i in PrimeNumbers(1, 30)])

"""
    3. 如何进行反向迭代以及如何实现反向迭代？
"""
print('\n\n\n-----3. 如何进行反向迭代以及如何实现反向迭代？-----')

l = [i for i in range(5)]
l_r = reversed(l)  # 反向迭代器
l_i = iter(l)  # 正向迭代器


class FloatRange:
    def __init__(self, start, end, step):
        self.start, self.end, self.step = start, end, step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


print([i for i in FloatRange(1, 2, 0.2)])  # [1, 1.2, 1.4, 1.5999999999999999, 1.7999999999999998, 1.9999999999999998]
print([i for i in
       reversed(FloatRange(1, 2, 0.2))])  # [2, 1.8, 1.6, 1.4000000000000001, 1.2000000000000002, 1.0000000000000002]

"""
    4. 如何对迭代器做切片操作？ 
    -   读取文本的100~300行
"""
print('\n\n\n-----4. 如何对迭代器做切片操作？-----')

from itertools import islice

with open('my_screen.py', 'r') as f:
    print([i for i in islice(f, 10, 20)])

l = [i for i in range(20)]
l_i = iter(l)
# islice 会消耗迭代器对象
print([i for i in islice(l_i, 3, 5)])  # [3, 4]
print([i for i in l_i])  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

"""
    5. 如何在一个for语句中迭代多个可迭代对象？
"""
print('\n\n\n-----5. 如何在一个for语句中迭代多个可迭代对象？-----')

math = [random.randint(60, 100) for _ in range(20)]
english = [random.randint(60, 100) for _ in range(20)]

print(list(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd'])))  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# 并行    zip 将多个可迭代对象进行打包操作
print([i for i in zip(math,
                      english)])  # [(99, 96), (62, 68), (92, 84), (78, 78), (66, 97), (83, 69), (67, 79), (74, 75), (97, 86), (100, 91), (100, 96), (65, 88), (67, 84), (80, 61), (93, 91), (65, 60), (75, 91), (80, 64), (71, 68), (97, 96)]

# 串行 chain 将多个可迭代对象进行连接操作
from itertools import chain

print([x for x in chain(math,
                        english)])  # [99, 62, 92, 78, 66, 83, 67, 74, 97, 100, 100, 65, 67, 80, 93, 65, 75, 80, 71, 97, 96, 68, 84, 78, 97, 69, 79, 75, 86, 91, 96, 88, 84, 61, 91, 60, 91, 64, 68, 96]
