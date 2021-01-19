#把上次作业改成 pytest 数据驱动模式，
#定义一个 autouse 的夹具，在用例执行前 ”打开数据库“， 执行后 ”关闭数据库“
#生成 allure 测试报告。（命令写在注释，提供报告截图或者运行视频）
import pytest
data = [
    {"username":"yuz","password":"123456","expected":"登录成功"},
    {"username":"zc","password":"123456","expected":"登录失败"},
    {"username":"yuz","password":"12345","expected":"登录失败"},
    {"username":"","password":"123456","expected":"登录失败"},
    {"username":"yuz","password":"","expected":"登录失败"}
]

def login(username,password):
    if username == 'yuz' and password == '123456':
        return "登录成功"
    else:
        return "登录失败"

@pytest.fixture(autouse=True)
def function_before():
    print("打开数据库")
    yield
    print("关闭数据库")

@pytest.mark.parametrize('info',data)  #这里打断点怎么调试？怎么我F8，F7都会进入源码内部去了
def test_login(info):
    u = info['username']
    p = info['password']
    exp = info['expected']
    assert exp == login(u,p)

"""
生成allure测试报告命令
pytest --alluredir=zc_output
allure serve zc_output
"""


