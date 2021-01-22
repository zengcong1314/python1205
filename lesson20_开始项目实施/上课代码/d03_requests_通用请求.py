import requests

# 自动化测试用的最多的

url = 'http://httpbin.org/get?username=yuz&password=123'
header = {'xyz':'nana','content-type':'application/json'}
param = {}
data = {"age":18}
method = 'get'

# 通用请求
res = requests.request(method,url,headers=header,data=data)
print(res.json())
