"""
- get
- post
"""
import requests
# 发送 GET 请求
# 请求的接口地址：本地 http://host:port/user/login
# 写代码之前，先用 postman 手工测一把

url = 'http://httpbin.org/get'
header = {'xyz':'nana'}
data = {"username":"yuz","password":"123456"}
res = requests.get(url,params=data,headers=header)
print(res.json())
# HTML,XML
print(res.text)

#响应体的二进制的数据，图片，视频 b=bytes
print(res.content)
