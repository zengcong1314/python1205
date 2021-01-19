"""
开发写的后端接口 djanggo,flask
"""
import time

from flask import Flask,request

server = Flask(__name__)

@server.route('/')
def index():
    # 获取 token
    token = request.args.get('t','')
    if not token:
        return {"msg":"login first,get token"}
    user = token.split('@')[0]
    token_start_time = token.split('@')[1]
    if user =='yw' and time.time() - float(token_start_time) < 600:
        # 校验 token
        return {"msg":"success","data":"Welcome to py36"}
    return {"msg":"login first,get token"}

@server.route('/login')
def login():
    # 获取query string：url当中得参数
    username=request.args.get('username')
    password=request.args.get('password')

    ts =str(time.time())
    if username =='yw' and password == '123456':
        """返回token给前端"""
        return {
            "token":username + "@" + ts,
            "id":1,
            "username":"yuz"
        }
    return {"msg":"username or password is error"}
if __name__ == '__main__':
    server.run(debug=True)
#访问登录得到得时间点，到你访问其他接口得时间点看有没有超过其他时间，就是token算过期时间
