#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 11:25
# @Author  : zc
# @FileName: read_txt.py
# @Software: PyCharm
import json
import uuid

with open ("0603.txt",'r',encoding='UTF-8') as f:
    data = f.read()
cun = data.count('#prop')
for i in range(cun):
    val = str(uuid.uuid4())
    data = data.replace('#prop' + str(i) + '#', val)
if data:
    cun2 = data.count('#key')
    for i in range(38):
        format_index = str(i + 1)
        val2 = str(uuid.uuid4())
        data = data.replace('#key' + format_index + '#', val2)
print(data)
data2 = json.dumps(data)
print("hello:",data)
data3 = json.loads(data)
print(json.loads(data3))
