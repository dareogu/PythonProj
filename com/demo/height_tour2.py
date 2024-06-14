#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
@:param hei 高度
@:param cou 反弹次数
@author dareo_gu
@date 2019-7-31
'''


def heighttour(hei, cou):
    print('总高度为：', hei)
    tour = hei
    hei /= 2
    for i in range(1, cou + 1):
        if i == 1:
            print('总距离：{0},第{1}次反弹高度：{2}'.format(tour, i, hei))
        else:
            tour += hei * 2
            hei /= 2
            print('总距离：{0},第{1}次反弹高度：{2}'.format(tour, i, hei))


heighttour(100.0, 1019)
