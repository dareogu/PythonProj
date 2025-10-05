# -*- coding: utf-8 -*-

'''
@Time    : 2025/10/5 16:19
@Author  : Dareo Gu
@FileName: test_filter.py
@Software: PyCharm

filter() 函数是 Python 中的一个内置函数，用于过滤可迭代对象中的元素。它根据指定的函数对每个元素进行测试，保留那些返回值为 True 的元素，丢弃返回值为 False 的元素
filter(function, iterable)
'''


def isPositive(num):
    return num > 0


numbers = [1, 15, -3, 4, -30, 0, 7, -8, 19, 20]
result = filter(isPositive, numbers)
print(list(result))


strings = ["apple", "", "banana", None, "cherry"]

# 过滤掉空字符串和 None
result = filter(None, strings)

print(list(result))  # 输出: ['apple', 'banana', 'cherry']
