import requests
def send_request(url,method,data=None,header=None,json=None):
    """封装发送请求的代码,把每次都会变的数据放到请求参数中"""
    # url = ''
    # method = ''
    # data = ''
    # header = ''
    res = requests.request(method=method,
                     url=url,
                     data=data,
                     headers=header,
                     json=json)
    try:
        ret = res.json()
    except:
        ret = res.text
    # 后面需要用到什么数据，想获取什么值，就返回什么，函数没有返回，调用后得到None
    return ret

def demo_request():
    a = send_request('http://api.lemonban.com/futureloan/member/register','post')
    print("函数的返回值",a)

demo_request()