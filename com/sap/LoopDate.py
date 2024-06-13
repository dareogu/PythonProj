#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = '''1/1/200%d
'''

file = open("LoopDate.txt", "w")
for i in range(1, 5025, 1):
    pass
    j = (i - 1) % 5
    result = s % (j)
    file.write(result)
file.close()
