#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a = 'jkljdfljsdjflkaj'
print(str.capitalize(a))  # 第一个字母大写

print(str.count(a, 'j'))  # 返回 str 在 string 里面出现的次数

print(str.endswith(a, 'ka'))  # 检查字符串是否以 ka 结束

print(str.find(a, 'g'))  # 检测 str 是否包含在 string 中

li = ['hoho', 18]
print('my name is {} ,age {}'.format('hoho', 18))
# 'my name is hoho ,age 18'
print('my name is {1} ,age {0}'.format(10, 'hoho'))
# 'my name is hoho ,age 10'
print('my name is {1} ,age {0} {1}'.format(10, 'hoho'))
# 'my name is hoho ,age 10 hoho'
print('my name is {} ,age {}'.format(*li))
# 'my name is hoho ,age 18'

str = '*'
seq = ('a', 'b', 'c')
print(str.join(seq))  # a*b*c

print(a.upper())

b = '  54f54da fa5f 31 '
print(b.lstrip())  # 截掉 string 左边的空格

c = 'hello world ni hao 123!!'
print(c.ljust(50, "0"))  # 右对齐，剩余部分用0代替

d = 'cat dog niha kcat kjfdog catd'
print(d.replace('cat', 'bird'))  # 替换

e = 'www.runoob.com'
print(e.partition('o'))  # 分割('www.run', 'o', 'ob.com')
print(e.rpartition('o'))  # 从右开始分割('www.runoob.c', 'o', 'm')
print(e.split('.'))  # ['www', 'runoob', 'com']

f = '45fda jklfjd jievnzoi eik kafdfs'
ctrans = f.maketrans("aeiou", "12345")
print(f.count('k', 0, len(f)))
print(f.translate(ctrans))
