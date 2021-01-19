# 登录测开平台，并访问 projects 接口，获取数据。
# 接口地址：
# http://www.keyou.site:8000/user/login/    post请求，username 和 password 通过 json 格式传递
# http://www.keyou.site:8000/projects/        get请求，token 放在 headers 中传递
# 用户名：lemon1
# 密码：123456
# token 值放在 headers 的
# Authorization，前缀是 JWT + "空格" + token值
import requests
def http_request(url,data=None,method='post',Authorization=None):
    if method == 'post':
        res = requests.post(url,json=json)
    else:
        method == 'get'
        res = requests.get(url, params=data,headers={"Authorization":Authorization})
    return res



if __name__ == '__main__':
    url = 'http://www.keyou.site:8000/user/login/'
    json = {
        "username":"lemon1",
        "password":123456
    }
    res = http_request(url,json,'post')
    print(res.json())
    token1 = res.json()['token']
    print(token1)
    Authorization2 = 'JWT' + ' ' + token1
    url1 = 'http://www.keyou.site:8000/projects/'
    data1 = None
    res2 = http_request(url1,data1,'get',Authorization2)
    print(res2.text)