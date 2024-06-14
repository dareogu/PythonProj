#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = '''C%d
C%d
C%d
C%d
C%d
'''

file = open("loop_code2.txt", "w")
for i in range(1, 2001):
    pass
    result = s % (i, i, i, i, i)
    file.write(s)
file.close()
