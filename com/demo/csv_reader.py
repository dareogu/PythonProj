# -*- coding:gbk -*-
import csv
#TODO
with open(r'D:\pyProjects\Test01.csv') as f:
    datareader = csv.reader(f)
    print(list(datareader))
