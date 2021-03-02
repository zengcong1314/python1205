from flask import Flask,request

# 初始化服务对象
app = Flask(__name__)

@app.route('/member/register')
def register():
    # 获取请求参数，
    username = request.args.get("username")
    if not username:
        return  {"msg":"no username"}
    return {"msg":"ok","data":{"token":"adssdsfdsfgg"}}

@app.route('/member/login')
def login():
    return {"msg":"ok","data":{"token":"adssdsfdsfgg"}}

if __name__ == '__main__':
    app.run()


