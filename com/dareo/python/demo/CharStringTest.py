#!/usr/local/bin/python3.8
# encoding: utf-8
'''
字符串的使用方法
Created on 2018年5月12日

@author: Dareo_Gu
'''
name = 'apple'
print(name[2:])  # 索引从0开始，打印的是第三个字母直至最后的字符串
if name.startswith('ap'):
    print('Yes, start with ap')
if 'a' in name:
    print('Yes, it contains "a"')
if name.find('le'):
    print('Yes, it contains "le"')
delimiter = '****'  # 分隔符
country = ['China', 'Russia', 'India', 'Brazil']
print(delimiter.join(country))  # China****Russia****India****Brazil
print(name.upper())  # 转换成大写
