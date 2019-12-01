#!/usr/local/bin/python3.8
# encoding: utf-8
'''
比较extend和append所消耗的时间
Created on 2018年5月13日
@author: Dareo_Gu
'''
import time
def dur(op,clock):
    duration=time.time()-clock  #time.time()表示当前时间 floating point number
    print('%s is finished, it cost %.6f seconds' % (op, duration))  # %.6f

list1=[]
f1=time.time() 
for i in range(1000):
    for j in range(1000):
        list1.append(j)
dur("List1 append", f1)

list2=[]
f2=time.time() 
seq=range(1000)
for j in range(1000):
    list2.extend(seq)
dur("List2 extend", f2)
