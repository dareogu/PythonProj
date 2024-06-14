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

c = math.modf(12.302)
print(c)

d = random.randrange(1, 10000, 3)
print(d)
