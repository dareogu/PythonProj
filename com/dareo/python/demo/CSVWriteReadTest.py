#!/usr/local/bin/python3.8
# encoding=utf-8
'''
Created on 2018年2月27日

@author: Dareo_Gu
'''
import csv

# 写CSV
file1 = open('csv_demo.csv', 'w')
spamwriter = csv.writer(file1, delimiter=',')
spamwriter.writerow(['aaa', 'bbb', 'ccc'])
  
file1.close()

# 读CSV
file2 = open('csv_demo.csv', 'r')
reader = csv.reader(file2, delimiter=',')
for row in reader:
    print(row)
    # 遍历每行中的每个数据
    for data in row:
        print(data)
file2.close()
