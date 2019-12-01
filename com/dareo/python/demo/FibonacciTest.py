#!/usr/local/bin/python3.8
# encoding: utf-8
'''
打印斐波那契数列

Created on 2018年5月6日

@author: Dareo_Gu
'''
n=int(input('please Enter the value of n(n>2)：'))

f0=1
f1=1
if n<=2:
    print(f0, f1)
else:
    print(f0, f1, end=' ')
    for i in range(n-2):
        f=f0+f1
        f0=f1
        f1=f
        print(f, end=' ')

        