# -*- coding: utf-8 -*-

'''
@Time    : 2025/10/5 10:46
@Author  : Dareo Gu
@FileName: test_decorator.py
@Software: PyCharm

在 Python 中，装饰器（Decorator）是一种用于修改或增强函数或方法行为的设计模式。简单来说，装饰器是一个函数，它接受一个函数作为输入，并返回一个新的函数，通常是对原函数行为的修改或扩展。

装饰器的基本概念：
装饰器是 Python 中的一种语法结构，它允许你在不修改函数源代码的情况下，增加额外的功能。装饰器通常用于日志记录、权限检查、性能计时等场景。

语法：
装饰器的语法通过 @decorator_name 来使用：

Python 提供了一些内置的装饰器，如 @staticmethod, @classmethod, 和 @property，这些装饰器用于改变方法的行为。

@staticmethod：用于将类中的方法定义为静态方法。
@classmethod：用于将方法定义为类方法。
@property：用于将方法转换为属性。
'''

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# 使用装饰器
@my_decorator
def say_hello():
    print("Hello, world!")

# 调用 say_hello
say_hello()
