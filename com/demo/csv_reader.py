# -*- coding:gbk -*-
import csv
#TODO
with open('D:\pyProjects\Test01.csv') as f:
    datareader = csv.reader(f)
    print(list(datareader))
