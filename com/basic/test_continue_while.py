#!/usr/local/bin/python3.8
# encoding: utf-8
'''
Practice while continue break

Created on 2018年5月5日
@author:     Dareo_Gu
@contact:    njhmwx@163.com

'''
i = 0
while True:
    s = input('s--->')
    if s == 'quit':
        break
    if len(s) < 3:
        print('sorry!')
        continue  # 跳出当前循环，继续下次循环
    i += 1
    print('length of the string is ', len(s))
print('i=', i)
print('done!')
