#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a = ["a"]
b = a * 3
print(b)

# 对于s * n操作，s序列中的元素没有被复制，他们只是被引用了多次
c = [["c"]]
d = c * 3
print(d)
e = c[0].append("c1")
print(d)

#列表切片 list[start:stop:step]
f = [0,1,2,3,4,5,6,7,8,9]
print(f[:2]) #=> [0, 1]
print(f[8:]) #=> [8, 9]
print(f[2:8]) #=> [2, 3, 4, 5, 6, 7]
print(f[2:8:2]) #=> [2, 4, 6]
