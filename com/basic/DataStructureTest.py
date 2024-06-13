#!/usr/local/bin/python3.8
# encoding: utf-8
'''
1****数据结构：列表，元组，字典
Created on 2018年5月12日

@author: Dareo_Gu
'''
# 1列表
storage_box = ['pen', 'pencil', 'eraser', 'scissors']
print('I have', len(storage_box), 'items.')
print('These item are:', end=' ')
for item in storage_box:
    print(item, end=' ')
print('\nI also hava to buy glue.')
storage_box.append('glue')  # 加入一个元素
print('Now I have', storage_box)
print('I will sort my list now')
storage_box.sort()  # 排序
print('Sorted slit is', storage_box)
print('The first item I have is', storage_box[0])
olditem = storage_box[0]
del storage_box[0]  # 删除第一个元素
print('I lost the', olditem)
print('Now I have', storage_box)

# 2元组值是不可改变的
a = (1, 2, 3, 4)
# del a[0]  TypeError: 'tuple' object doesn't support item deletion
# a[0]=5  TypeError: 'tuple' object does not support item assignment

garden = ('rose', 'azelea', 'mum')
print('Number of flowers in the garden is', len(garden))
new_garden = ('peony', 'orchid', garden)
print('Number of flowers in the new garden is', len(new_garden))
print('All flowers in new garden are', new_garden)  # ('peony', 'orchid', ('rose', 'azelea', 'mum'))
print('Flowers brought from old garden are', new_garden[2])
print('Last flower brought from old garden is', new_garden[2][2])

num = 15
fruit = 'apple'
name = 'Dareo'
print('%s have %d %s' % (name, num, fruit))

# 元组内置函数
# 元组比较 cmp(tuple1, tuple2)
# 元组个数 len（tuple）
# 元组中最大最小值 max（tuple），min（tuple）
# **将列表转换为元组***
print(tuple(storage_box))  # ('glue', 'pen', 'pencil', 'scissors')

# 3字典
ab = {'Jack': "jackma@alibaba.com", "Pony": "pony@qq.com", "David": "david@hotmail.com", "Jay": "jay.sun@sohu.com"}
print("Jay's email is %s" % ab['Jay'])
ab['Jim'] = 'jim@live.com'  # 增加一个键值对
del ab['David']
print('\nThere are %d contact in the email book\n' % len(ab))
for name, email in ab.items():
    print('Contact %s at %s' % (name, email))
    if 'David' in ab:
        print("\nPang's email is %s" % ab['David'])
print(ab.keys())  # 返回一个包含缩减键的列表 ab.values()
print(ab.items())  # 返回一个列表，列表元素由（key,value）的元组 构成，如下
# [('Jim', 'jim@live.com'), ('Jay', 'jay.sun@sohu.com'), ('Pony', 'pony@qq.com'), ('Jack', 'jackma@alibaba.com')]
# Python 2.7
# print(ab.has_key('Pony'))  # 判断是否还有key，如有，则为true，否则为false
