#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 19:36
# @Author  : zc
# @FileName: 2.py
# @Software: PyCharm
import json
import copy
import uuid
with open ("1234.txt","r",encoding='UTF-8') as f:
    data = f.read()
temp_dict = json.loads(data)
new_dict = copy.deepcopy(temp_dict)
num = 1
var_dict={}
for key, value in new_dict.items():
    if isinstance(value, list):
        for i in range(len(value)):
            if isinstance(value[i], dict):
                if "prop" in value[i].keys():
                    val = '#prop' + str(num) + '#'
                    var_dict.update({new_dict[key][i]["prop"]: str(val)})
                    new_dict[key][i]["prop"] = str(val)
                    num+=1
            continue
print(json.dumps(new_dict, ensure_ascii=False))
with open ("12345.txt","w",encoding='UTF-8') as f2:
    f2.write(json.dumps(new_dict, ensure_ascii=False))