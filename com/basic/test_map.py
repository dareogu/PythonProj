# -*- coding: utf-8 -*-

'''
@Time    : 2025/10/5 16:08
@Author  : Dareo Gu
@FileName: test_map.py
@Software: PyCharm
'''
from functools import reduce


def square(x, y):
    return x ** y


list1 = [1, 2, 3, 9]
list2 = [4, 5, 6, 12]
result = map(lambda x, y: x * y, list1, list2)
print(list(result))

result2 = map(square, list1, list2)
print(tuple(result2))


def add(a, b):
    return a + b


# reduce() 会将可迭代对象中的元素通过累积的方式（通常是递归式地）结合起来，从而得到一个最终的结果
result = reduce(add, list1)
print(result)
