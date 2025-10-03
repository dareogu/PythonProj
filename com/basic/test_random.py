# -*- coding: utf-8 -*-

'''
@Time    : 2025/10/3 12:26
@Author  : Dareo Gu
@FileName: test_random.py
@Software: PyCharm

总结
random.randint(a, b)：生成范围 [a, b] 内的随机整数。
random.uniform(a, b)：生成范围 [a, b] 内的随机浮动数。
random.choice(seq)：从序列 seq 中随机选择一个元素。
'''

import random

'''
生成指定长度的随机整数列表
'''
numberList = [random.randint(1, 100) for count in range(10)]
print(numberList) #[15, 53, 47, 60, 69, 12, 65, 50, 73, 54]

'''
生成一个长度为 10，范围在 -1.0 到 1.0 之间精度为3的随机浮动数列表
'''
floatList = [round(random.uniform(-1.0,1.0),3) for count in range(10)]
print(floatList) #[0.93, 0.517, -0.993, 0.609, 0.03, 0.777, 0.888, 0.747, 0.417, -0.018]

fruits = ['apple', 'banana', 'orange', 'grapes', 'cherry']

'''
用于 从指定序列或集合中随机抽取指定数量的独立元素，且不会重复,它返回的是一个新的列表
random.sample(population, k)
1.population：可以是列表、元组、字符串等可迭代对象
2.k：要抽取的元素数量，必须不大于 population 的长度
3.返回值：长度为 k 的列表，元素随机且不重复

例
# 生成长度为5的随机不重复整数列表，范围 0~9
[2, 7, 0, 5, 8]
numbers = random.sample(range(10), 5)
print(numbers)

s = "abcdefg"
chars = random.sample(s, 3)  # 随机抽取 3 个字符
print(chars)
'''
random_sample_list = random.sample(fruits, 3)
print(random_sample_list)

'''
生成指定长度的随机选择列表（从指定的列表中随机选择）
'''
random_choice_list = [random.choice(fruits) for _ in range(10)]
print(random_choice_list) #['banana', 'banana', 'grapes', 'grapes', 'apple', 'apple', 'apple', 'cherry', 'apple', 'grapes']
