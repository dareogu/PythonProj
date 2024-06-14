#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''

for i in range(2, 85, 2):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            n = int((i - j) / 2)
            x = n * n - 100
            print(x)
