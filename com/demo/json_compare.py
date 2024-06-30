# -*- coding: utf-8 -*-

'''
@Time    : 2024/6/21 22:54
@Author  : Dareo Gu
@FileName: json_compare.py
@Software: PyCharm

Python常见Json对比库deepdiff、json_tools、jsonpatch
'''

import json
from deepdiff import DeepDiff
import json_tools
from jsonpatch import JsonPatch


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def deepdiff_compare(json_a, json_b):
    result = DeepDiff(json_a, json_b)
    print(result)


def json_tools_compare(json_a, json_b):
    result = json_tools.diff(json_a, json_b)
    print(result)


def jsonpatch_compare(json_a, json_b):
    result = JsonPatch.from_diff(json_a, json_b)
    print(result)


a = {"name": "yanan", "pro": {"sh": "shandong", "city": ["zibo", "weifang"]}}
b = {"name": "Yanan", "pro": {"sh": "shandong", "town": ["taian", "weifang"]}}
c = load_json('json_c.json')
d = load_json('json_d.txt')

# 对比不同
# {'dictionary_item_added': [root['pro']['town']], 'dictionary_item_removed': [root['pro']['city']], 'values_changed': {"root['name']": {'new_value': 'Yanan', 'old_value': 'yanan'}}}
deepdiff_compare(a, b)

# [{'replace': '/name', 'value': 'Yanan', 'prev': 'yanan'}, {'remove': '/pro/city', 'prev': ['zibo', 'weifang']}, {'add': '/pro/town', 'value': ['taian', 'weifang']}]
json_tools_compare(c, d)

# [{"op": "remove", "path": "/pro/city"}, {"op": "add", "path": "/pro/town", "value": ["taian", "weifang"]}, {"op": "replace", "path": "/name", "value": "Yanan"}]
jsonpatch_compare(a, b)

# 对比一样
deepdiff_compare(a, a)
json_tools_compare(c, c)
jsonpatch_compare(d, d)
