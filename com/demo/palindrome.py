#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = input('请输入一个数：\n')

len = len(a)
flag = True

for i in range(int(len / 2)):
    if a[i] != a[len - 1 - i]:
        flag = False
        break
if flag:
    print('是一个回文数')
else:
    print('不是一个回文数')
