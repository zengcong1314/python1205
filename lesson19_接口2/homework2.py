# 登录测开平台，并访问 projects 接口，获取数据。
# 接口地址：
# http://www.keyou.site:8000/user/login/    post请求，username 和 password 通过 json 格式传递
# http://www.keyou.site:8000/projects/        get请求，token 放在 headers 中传递
# 用户名：lemon1
# 密码：123456
# token 值放在 headers 的
# Authorization，前缀是 JWT + "空格" + token值
import requests
def login(url,data):
    res = requests.post(url,json=data)

    print(res.json())
    return res
def query(url,data,token):
    authorization = 'JWT' + ' ' + token
    res = requests.get(url,params=data,headers={"Authorization":authorization})
    print(res.text)
    return res

url = 'http://www.keyou.site:8000/user/login/'
data = {
        "username":"lemon1",
        "password":123456
        }
res = login(url,data)
token = res.json()['token']
print(token)
url1 = 'http://www.keyou.site:8000/projects/'
data1 = None
res2 = query(url1,data1,token)
print(res2)
