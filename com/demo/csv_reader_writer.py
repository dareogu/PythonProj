#!/usr/local/bin/python3.8
# encoding=utf-8
'''
Created on 2018年2月27日

@author: Dareo_Gu
'''
import csv

# 写CSV 一行
file1 = open('csv_demo.csv', 'w', newline='', encoding='utf-8')  # newline='' 避免空行
writer = csv.writer(file1, delimiter=',')
writer.writerow(['aaa', 'bbb', 'ccc'])
file1.close()

# 写CSV 多行
data = [('zzz', 20, 123456), ('jojo', 10, 789012)]
writer = csv.writer(open('writer_demo.csv', 'w', newline=''))
writer.writerows(data)

# 读CSV 1
file2 = open('csv_demo.csv', 'r')
reader = csv.reader(file2, delimiter=',')
for row in reader:
    print(row)
    # 遍历每行中的每个数据
    for data in row:
        print(data)
file2.close()

# 读CSV 2
with open(r'csv_demo.csv') as f:
    reader = csv.reader(f)
    print(list(reader))
