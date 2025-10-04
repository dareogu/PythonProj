# -*- coding: utf-8 -*-

'''
@Time    : 2025/10/4 21:58
@Author  : Dareo Gu
@FileName: get_right_number.py
@Software: PyCharm

一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
设这个整数为 x,那么，根据问题则
x+100=a**2
x+268=b**2

(b−a)(b+a)=168，且 b-a 和 b+a 都为偶数
'''


def find_number():
    for i in range(2, 85, 2): #168两个因子都是偶数
        if 168 % i == 0:
            j = 168 / i
            if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
                n = int((i - j) / 2)
                x = n * n - 100
                print(x)


find_number()
