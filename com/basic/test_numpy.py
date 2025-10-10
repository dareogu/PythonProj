# -*- coding: utf-8 -*-

'''
@Time    : 2025/10/5 17:12
@Author  : Dareo Gu
@FileName: testNumPy.py
@Software: PyCharm
'''

import numpy as np

##使用 numpy.array()
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
ab = np.concatenate((a, b))  # => array([1, 2, 3, 4, 5, 6])
print(type(ab))  # numpy.ndarray
print(ab)  # [1 2 3 4 5 6]

##使用 numpy.arange() 创建数值范围
arr = np.arange(0, 10, 2)  # 从 0 到 10 之间步长为
print(arr)  # [0 2 4 6 8]

##使用 numpy.zeros() 和 numpy.ones() 创建全零或全一数组
# 创建一个 3x3 的全零数组
zeros_arr = np.zeros((3, 3))
print(zeros_arr)
# 输出:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

# 创建一个 2x4 的全一数组
ones_arr = np.ones((2, 4))
print(ones_arr)
# 输出:
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# 使用 numpy.linspace() 创建等间距数组
# 创建一个包含 5 个元素的数组，范围从 0 到 1（包括 0 和 1）
linspace_arr = np.linspace(0, 1, 5)
print(linspace_arr)
# 输出: [0.   0.25 0.5  0.75 1.  ]

# 数组的形状和大小
arr_oper = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape:", arr_oper.shape)  # 输出: (2, 3)
print("Size:", arr_oper.size)  # 输出: 6
print("Data type:", arr_oper.dtype)  # 输出: int64

# 索引和切片
arr_test = np.array([10, 20, 30, 40, 50])

# 获取第一个元素
print(arr_test[0])  # 输出: 10

# 获取最后一个元素
print(arr_test[-1])  # 输出: 50

# 切片操作
print(arr_test[1:4])  # 输出: [20 30 40]

# 对于多维数组，可以使用类似矩阵的切片方法
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 获取第 2 行，第 3 列的元素
print(arr2d[1, 2])  # 输出: 6

# 获取前两行的所有列
print(arr2d[:2, :])  # 输出: [[1 2 3]
#       [4 5 6]]

# 数学运算
# 向量化运算
arr1 = np.array([1, 2, 3])

# 数组与常数相加
print(arr1 + 5)  # 输出: [6 7 8]

# 数组与常数相乘
print(arr1 * 2)  # 输出: [2 4 6]

# 数组的平方
print(arr1 ** 2)  # 输出: [1 4 9]

# 数组间的运算
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # 输出: [5 7 9]

# 广播（Broadcasting）
# 它允许不同形状的数组进行数学运算，NumPy 会自动将较小的数组扩展（或广播）到与较大数组匹配的形状
arr3 = np.array([1, 2, 3])
arr4 = np.array([10])

# 广播：将 arr4 中的 10 加到 arr3 的每个元素上
print(arr3 + arr4)  # 输出: [11 12 13]

# 常用函数
# np.sum(arr)：求数组元素的和
# np.mean(arr)：计算数组元素的平均值
# np.median(arr)：计算数组的中位数
# np.std(arr)：计算数组的标准差
# np.min(arr) / np.max(arr)：返回最小值/最大值
array = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(array))  # 输出: 15
print("Mean:", np.mean(array))  # 输出: 3.0
print("Max:", np.max(array))  # 输出: 5

#重塑数组
arrays = np.array([1, 2, 3, 4, 5, 6])

# 将数组重塑为 2 行 3 列
reshaped_arr = arrays.reshape(2, 3)
print(reshaped_arr)
# 输出:
# [[1 2 3]
#  [4 5 6]]
