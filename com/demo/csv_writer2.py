# - * -coding: gbk - * -
import csv
#TODO
with open('E:\python\Test01.csv', 'wb') as f:
    w = csv.writer(f)

s = ('User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7')

user = []
for j in range(2):
    for i in s:
        user.append(i)

s.writer(f)
