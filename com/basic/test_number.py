#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import random

b = 2 ** 0.5
a = complex(12, 5.3)  # 复数

print(a)
print(type(a))

print(b)
print(type(b))

print(a + b)
print(type(a + b))

#用于将一个浮点数分解为两个部分：小数部分和整数部分,返回一个 元组,第一个值是浮动的小数部分,第二个值是浮动的整数部分
c = math.modf(12.302)
print(c)

d = random.randrange(1, 10000, 3)
print(d)
