# - * -coding: utf-8 - * -
import csv

with open(r'user.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    s = ('User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7')
    #每个字符一列，最后生成一个5列7行的csv文件
    writer.writerows(s)

    #每个元祖元素一列，最后生成一个1列7行的csv文件
    for item in s:
        writer.writerow((item,))
