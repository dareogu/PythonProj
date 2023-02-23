#!/usr/local/bin/python3.8
# encoding: utf-8
'''
1***全局变量 global关键字***
2***设置参数默认值***
3***可使用名字（关键字）而不是位置来给函数指定实参
4***文档字符串***

Created on 2018年5月6日
@author: Dareo_Gu
'''


def changeLocalValue(x):
    # global x  申明x为全局变量，不是局部变量
    print('x is', x)
    x = 2
    print('changed local x to', x)


x = 50
changeLocalValue(x)
print('Now x is', x)


# def eat(fruit='apple'，dessert):  不能把含默认值的参数放在不含默认值的参数之前，否则报错
def eat(desserts, fruit='apple'):
    print("I like", desserts)
    print("I like", fruit)


eat('chocolate')  # 缺省值fruit取默认值apple
eat('icecream', 'banana')


def printValues(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


printValues(3, 7)  # a is 3 and b is 7 and c is 10
printValues(25, c=24)  # a is 25 and b is 5 and c is 24
printValues(c=50, a=100)  # a is 100 and b is 5 and c is 50


def hi():
    '''This is one simple demo'''
    print('hello world')


hi()  # hello world
# None 没有return语句的函数也有返回值，结尾暗含有return None语句！！！
print(hi())  # hello world
print(hi.__doc__)  # This is a sample demo
