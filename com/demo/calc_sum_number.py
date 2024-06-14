#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
求s=a+aa+aaa+aaaa+aa...a的值
'''
Tn = 0
n = int(input('n = '))
a = int(input('a = '))

while a > 9 or a < 0:
    a = int(input('请重新输入a的值：'))

for i in range(0, n):
    Tn += (n - i) * a * (10 ** i)

print('值的总和为：', Tn)
