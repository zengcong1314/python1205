"""
开发写的后端接口 djanggo,flask
"""
import time

#SECRET_KEY = 'FFSFSF'


from flask import Flask,request,session

server = Flask(__name__)
server.config['SECRET_KEY'] = 'FFSFSF'
#session = []

@server.route('/')
def index():
    user = session.get('user','')
    if user == 'yw':
        return {"msg":"success","data":"100wan"}
    return {"msg":"login first,get session"}

@server.route('/login')
def login():
    # 获取query string：url当中得参数
    username=request.args.get('username')
    password=request.args.get('password')

    ts =str(time.time())

    if username =='yw' and password == '123456':
        session['user'] = username
        return {
            "msg":"login success"
        }
    return {"msg":"username or password is error"}

if __name__ == '__main__':
    server.run(debug=True)

# 采用session机制，返回set-cookie头，里面包含session用户信息
# 设置响应头之后，登录成功
# 保存在服务端得用户数据，就叫做session，这个用户数据直接通过加密（框架完成）自动放到响应头里面，自动设置字段Set-Cookie
# cookie自动保存在浏览器里面，
# 访问其他接口，首页时，cookie是域名和IP绑定在一起得
# 访问某个域名时，客户端自动在浏览器缓存中查找，有没有这个域名下得cookie，有就自动带上去，
# 当我们访问某个域名时，这些session自动带到cookie 得header里面

