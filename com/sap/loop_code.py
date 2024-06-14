#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = '''%d
%d
%d
%d
%d
%d
%d
%d
%d
%d
'''

file = open("loop_code.txt", "w")
for t in range(1, 1001, 1):
    pass
    i = t % 10 + 1
    result = s % (i, i, i, i, i, i, i, i, i, i)
    file.write(result)
file.close()
