import json

a = '{"name":"yuz","female":true}'
print(type(a))
b = json.loads(a)
print(type(b))

# 序列化和反序列化
# 充值
# 用例的依赖，登录功能