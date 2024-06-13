#!/usr/local/bin/python3.8
# encoding: utf-8
'''
1***如何导入模块
2***只想程序本身被只用的时候运行主块，而被其他模块导入时不运行，可使用模块的__name__属性实现***

Created on 2018年5月8日

@author: Dareo_Gu
'''
import sys

# 当前可用的属性和方法列表
print(dir())
# sys模块中可用的属性和方法列表
print(dir('sys'))
# sys模块的说明文档
print(sys.__doc__)

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('This program is being imported')
