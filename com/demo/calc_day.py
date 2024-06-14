#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
输入某年某月某日，判断这一天是这一年的第几天？
'''
year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sumDays = months[month - 1]
else:
    print
    'data error'
sumDays += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sumDays += 1
print('it is the %dth day.' % sumDays)
