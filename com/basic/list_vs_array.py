# -*- coding: utf-8 -*-

'''
@Time    : 2025/10/5 18:32
@Author  : Dareo Gu
@FileName: list_vs_array.py
@Software: PyCharm
'''

import timeit
import numpy as np

# 列表
list_test = timeit.timeit('sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])', number=1000000)

# 数组（NumPy）
array_test = timeit.timeit('np.sum(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))', setup="import numpy as np", number=1000000)

#当数据集很小时，sum() 的性能差异微乎其微，或者 NumPy 在初始化数组时的开销反而可能影响性能
print(list_test)  #0.08015240007080138
print(array_test)    #2.2848962999414653

# 创建一个包含 1 千万个数字的列表
large_list = list(range(1, 10000001))

# 创建一个包含 1 千万个数字的 NumPy 数组
large_array = np.array(range(1, 10000001))

# 列表求和
list_test = timeit.timeit('sum(large_list)', globals=globals(), number=10)

# NumPy 数组求和
array_test = timeit.timeit('np.sum(large_array)', setup="import numpy as np", globals=globals(), number=10)

print(f"列表求和时间: {list_test}")  # 1.5596661999588832
print(f"数组求和时间: {array_test}") # 0.056414399994537234
