#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import math

count = 0
for num in range(2, 10001):  # 迭代 1 到 100 之间的数字
    for i in range(2, int(math.sqrt(num) + 1)):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 为合数，因式分解%d 等于 %d * %d' % (num, num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print(num, '是一个质数')
        count += 1
print('一共存在', count, '个质数')
