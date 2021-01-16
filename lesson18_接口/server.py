"""
开发写的后端接口 djanggo,flask
"""
from flask import Flask

server = Flask(__name__)

@server.route('/')
def index():
    return {"msg":"success","data":"Welcome to py36"}

@server.route('/login')
def login():
    return """<p style="color:red">login</p>"""

if __name__ == '__main__':
    server.run(debug=True)

