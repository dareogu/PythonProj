# -*- coding: utf-8 -*-

'''
@Time    : 2025/10/5 21:25
@Author  : Dareo Gu
@FileName: csv_pandas.py
@Software: PyCharm

Series：一维带标签数组
DataFrame：二维表格型数据
核心操作：选择、筛选、修改、统计、缺失值处理
数据读取：CSV、Excel、JSON
性能优势：比原生 Python 列表和字典处理大数据更快

'''
import json
import warnings

import pandas as pd

warnings.simplefilter(action='ignore', category=FutureWarning)  # 忽略 FutureWarning

####### 数据结构 #######
# 从列表创建 Series
s = pd.Series([10, 20, 30, 40])
print(s)

# 自定义索引
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# s[0] 或 s['a'] 都可以访问元素
# Series 支持向量化运算，例如 s * 2、s + 5
print(s)
print(s[0])
print(s['b'])

# DataFrame（二维表格数据）
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Beijing', 'Shanghai', 'Guangzhou']
}

df = pd.DataFrame(data)
# df = df.set_index('name') #将'name'列设为新索引，替代默认整数索引，实际上就能做到去除整数索引的目的
# reset_index(drop=True) #会将原索引重置为默认的整数索引（0, 1, 2...），drop=True 表示删除原索引列，不将其保留为新的列（若不设置 drop=True，原索引会成为一个新列 index）
print(df)

print("打印时隐藏索引：")
print(df.to_string(index=False))

print(df['age'])  # 获取某一列（返回 Series）
print(df[['name', 'city']])  # 获取多列（返回 DataFrame）
print(df.loc[0])  # 获取第一行（按标签）
# name      Alice
# age          25
# city    Beijing
print(df.iloc[0])  # 获取第一行（按位置索引）

####### 读取/保存数据 #######
# 从 CSV 文件读取
csv = pd.read_csv('../data/csv_demo.csv')  # 文件路径
print(csv)

# 保存为 CSV
df.to_csv('../data/DataFrame.csv', index=False)  # 保存为CSV时不包含索引（index=False）
df_save = pd.read_csv('../data/DataFrame.csv')  # 文件路径
print(df_save)

# Excel: pd.read_excel() / df.to_excel()
excel = pd.read_excel('../data/Account.xlsx')
print(excel)
df.to_excel('../data/Employee.xlsx', index=False)
excel_save = pd.read_excel('../data/Employee.xlsx')
print(excel_save)

# JSON: pd.read_json() / df.to_json()
# 示例1：读取JSON字符串
json_str = '''
{"name": "yanan", "pro": {"sh": "shandong", "city": ["zibo", "weifang"]}}
'''
json_1 = pd.read_json(json_str)
print(json_1)
# 示例2：读取JSON文件
json_2 = pd.read_json('../data/json_c.json')
print(json_2)

# 示例3：处理嵌套JSON（通过orient参数指定格式）
nested_json = '''
[
  {"id": 1, "info": {"name": "Alice", "age": 25}},
  {"id": 2, "info": {"name": "Bob", "age": 30}}
]
'''
# orient='records' 表示JSON是列表形式的记录
df_nested = pd.read_json(nested_json, orient='records')
print("\n处理嵌套JSON：")
print(df_nested)

# 展开嵌套列（可选）
df_flat = pd.json_normalize(json.loads(nested_json))
print("\n展开嵌套JSON：")
print(df_flat)
# 输出：
#    id info.name  info.age
# 0   1    Alice        25
# 1   2      Bob        30

####### 数据查看和基本操作 #######
df_json = pd.read_json('../data/pandas_demo.json')
print(df_json)
print(df_json.head(1))  # 默认前5行
print(df_json.tail(2))  # 后2行

# 查看信息
print(df_json.info())  # 数据类型和非空情况
print(df_json.describe())  # 数值列统计信息
print(df_json.shape)  # 数据行列数 (rows, columns)
print(df_json.columns)  # 列名
print(df_json.index)  # 行索引

####### 数据选择和过滤 #######
print(df_json['externalCode'])  # 选择列
print(df_json.iloc[0])  # 按位置
print(df_json.loc[2])  # 按索引标签

# 条件筛选
print(df_json[df_json['index'] > 8])  # 筛选 index > 8 的行

# 多条件筛选
print(df_json[(df_json['index'] > 4) & (df_json['externalCode'] == 'admin2')])

####### 数据修改 #######
# 添加新列
df_json['salary'] = [9000, 6500, 5300, 7000]
print(df_json)
df_json_original = df_json.copy(deep=True)  # deep copy
df_value_sorted = df_json.sort_values(by='salary', ascending=False)  # 按列 salary 降序
print("\n按照列排序后：")
print(df_value_sorted)
df_index_sorted = df_json.sort_index(ascending=False)  # 按 index 降序
print("\n按照索引排序后：")
print(df_index_sorted)

# 修改列
df_json['index'] = df_json['index'] + 1
print(df_json[['externalCode', 'index']])

# 删除列
df_json.drop('salary', axis=1, inplace=True)
print(df_json)  # salary这一列被整体删除

# 删除行
df_json.drop(0, axis=0, inplace=True)
print(df_json)  # 第一行被删除

####### 缺失值处理 #######
# 检查缺失值
df_null = df_json.isnull()
print(df_null)

# 删除缺失值
df_json.dropna(inplace=True)
print(df_json)

# 填充缺失值
df_json.fillna(0, inplace=True)
print(df_json)

####### 数据统计和汇总 #######
# 基本统计
print(df_json_original['age'].mean())  # 平均值
print(df_json_original['age'].sum())  # 总和
print(df_json_original['age'].max())  # 最大值
print(df_json_original['age'].min())  # 最小值

# 分组统计
df_groupby = df_json_original.groupby('category')['age'].mean()
print(df_groupby)

####### 数据统计和汇总 #######
# 合并两个 DataFrame（类似 SQL JOIN）
df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'id': [1, 2, 4], 'score': [90, 85, 80]})

merged = pd.merge(df1, df2, on='id', how='left')
print(merged)
