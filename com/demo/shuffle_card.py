# !/usr/bin/python
# -*- coding: UTF-8 -*-

import random

items = []
for i in range(1, 53):
    items.append(i)
'''将items进行乱序'''
random.shuffle(items)
for n in range(len(items)):
    if n % 13 == 0:
        print("")
    if items[n] < 14:
        if items[n] == 1:
            print('桃A ', end='')
        elif items[n] < 11:
            print('桃{} '.format(items[n]), end='')
        elif items[n] == 11:
            print('桃J ', end='')
        elif items[n] == 12:
            print('桃Q ', end='')
        else:
            print('桃K ', end='')
    elif 14 <= items[n] <= 26:
        if items[n] - 13 == 1:
            print('梅A ', end='')
        elif items[n] - 13 < 11:
            print('梅{} '.format(items[n] - 13), end='')
        elif items[n] - 13 == 11:
            print('梅J ', end='')
        elif items[n] - 13 == 12:
            print('梅Q ', end='')
        else:
            print('梅K ', end='')
    elif 27 <= items[n] <= 39:
        if items[n] - 26 == 1:
            print('心A ', end='')
        elif items[n] - 26 < 11:
            print('心{} '.format(items[n] - 26), end='')
        elif items[n] - 26 == 11:
            print('心J ', end='')
        elif items[n] - 26 == 12:
            print('心Q ', end='')
        else:
            print('心K ', end='')
    elif 40 <= items[n] <= 52:
        if items[n] - 39 == 1:
            print('砖A ', end='')
        elif items[n] - 39 < 11:
            print('砖{} '.format(items[n] - 39), end='')
        elif items[n] - 39 == 11:
            print('砖J ', end='')
        elif items[n] - 39 == 12:
            print('砖Q ', end='')
        else:
            print('砖K ', end='')
