#!/usr/local/bin/python3.8
# encoding: utf-8
'''
利用for循环在规定的次数内是否猜到随机整数的一个猜数游戏
Created on 2018年5月5日
@author: Dareo_Gu
'''

import random

number = random.randint(0, 300)
for i in range(10):
    guess = int(input('Please enter an integer:'))
    if guess == number:
        print('you are right, the number is', number)
        break
    elif guess > number:
        print('your number is higher, please reenter an integer!')
    else:
        print('your number is lower, please reenter an integer!')
else:
    print("game over!haha!")
print('number is ', number)
