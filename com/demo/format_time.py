#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

'''
暂停一秒输出，并格式化当前时间
'''
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
