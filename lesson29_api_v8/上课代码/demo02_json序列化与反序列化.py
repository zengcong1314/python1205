"""json格式字符串转化为python当中字典格式操作"""
import json

# json.load() # 处理文本流

# 是把json格式的字符串转化为python当中得字典，把通用数据格式转化为某一门语言的数据类型，叫做反序列化 loads
a = '{"username":"zc","pwd":"123456"}'
print(json.loads(a))

# 把python的字典转化成json 格式的字符串，把某一种语言的数据类型转化成json 通用格式叫做序列化 dumps
b = {"name":"zc","age":18}
json.dumps(b)
