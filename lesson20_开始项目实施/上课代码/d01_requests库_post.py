"""
- get
- post
"""
import requests
# 发送 POST 请求
# 请求的接口地址：本地 http://host:port/user/login
# 写代码之前，先用 postman 手工测一把
# POST 支持query string

url = 'http://httpbin.org/post?username=yuz&password=123456'
header = {'xyz':'nana','content-type':'application/json'}
data = {"age":18}
# requests 如果想传第form，使用data这个参数
res = requests.post(url,data=data,headers=header)
print(res.json())
# HTML,XML
print(res.text)

#响应体的二进制的数据，图片，视频 b=bytes
print(res.content)

# 传第json数据，content-type = 'application/json',json=data
res = requests.post(url,json=data,headers=header)
print(res.json())
# HTML,XML
print(res.text)