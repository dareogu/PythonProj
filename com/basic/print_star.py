#!/usr/local/bin/python3.8
# -*- coding: UTF-8 -*-

from sys import stdout

for i in range(4):
    for j in range(3 - i):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print()

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(5 - 2 * i):
        stdout.write('*')
    print()
