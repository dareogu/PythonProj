# -*- coding: utf-8 -*-

'''
@Time    : 2025/10/4 21:37
@Author  : Dareo Gu
@FileName: perfect_number.py
@Software: PyCharm
'''

def getDivisors(n):
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def is_perfect_number(n):
    divisors = getDivisors(n)
    divisors_sum = sum(divisors)
    if divisors_sum == n:
        print(f"{n}是一个完美数")
        print(f"它的因子是：{divisors}")

for n in range(1, 10000):
    is_perfect_number(n)
