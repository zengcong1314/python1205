#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 10:43
# @Author  : zc
# @FileName: ruuid.py
# @Software: PyCharm

import uuid

import jsonpath

res = uuid.uuid1()
# res5 = uuid.uuid5()
#res3 = uuid.uuid3()
# res4 = uuid.uuid4()

print(res)
#print(res5)
#print(res3)
# dic = {"prop":"3244345","prop2":"435675768"}
# res = jsonpath.jsonpath(dic,'$..prop')
# if "prop" in dic:
#     print(str(jsonpath.jsonpath(dic,'$..prop')))
#     print(str(uuid.uuid1()))
#     dic2= str(dic).replace(str(jsonpath.jsonpath(dic,'$..prop')),str(uuid.uuid1()))
#
#     print(dic2)

#生成一个字典
# d = {'name':{},'age':{},'sex':{}}
#打印返回值，其中d.keys()是列出字典所有的key
# print (name in d.keys())

import json
import copy
import uuid
with open ("0603.txt","r",encoding='UTF-8') as f:
    data = f.read()
# coun = data.count('#prop')
# for i in range(coun):
#     val = uuid.uuid4()
#     data = data.replace('#prop' + str(i+1) + '#', str(val))
# data = data.replace("'",'"')
#print(data)

temp_dict = json.loads(data)
#print("temp_dict数据为：",temp_dict)
new_dict = copy.deepcopy(temp_dict)
#print("new_dict数据为：",new_dict)
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
count = 1
for key, value in new_dict.items():
    if isinstance(value, list):
        for i in range(len(value)):
            if isinstance(value[i], dict):
                if isinstance(value[i]['options'],list):
                    for j in range(len(value[i]['options'])):
                        if "key" in value[i]['options'][j].keys():
                            val = '#key' + str(count) + '#'
                            var_dict.update({new_dict[key][i]['options'][j]["key"]: str(val)})
                            new_dict[key][i]['options'][j]["key"] = str(val)
                            count+=1
                continue

ct = 1
for key, value in new_dict.items():
    if isinstance(value, list):
        for i in range(len(value)):
            if isinstance(value[i], dict):
                if isinstance(value[i]['options'],list):
                    for j in range(len(value[i]['options'])):
                        if "nodeId" in value[i]['options'][j].keys():
                            val = '#nodeId' + str(ct) + '#'
                            var_dict.update({new_dict[key][i]['options'][j]["nodeId"]: str(val)})
                            new_dict[key][i]['options'][j]["nodeId"] = str(val)
                            ct+=1
                continue

print(json.dumps(new_dict, ensure_ascii=False))
#
# with open ("1234.txt","w",encoding='UTF-8') as f2:
#     f2.write(json.dumps(new_dict, ensure_ascii=False))

#print(var_dict)



