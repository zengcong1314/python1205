"""
fixture,测试夹具，测试用例执行的前置动作和后置动作
前置条件：
"""
import pytest

def login(username,password):
    """开发写的功能"""
    if username == 'yuz' and password == '123456':
        return "登录成功"
    else:
        return "登录失败"
data = [
    {"username":"yuz","password":"123456","expected":"登录成功"},
    {"username":"","password":"","expected":"登录失败"},
    {"username":"a","password":"b","expected":"登录失败"}
]
#哪个用例使用夹具，把夹具的名称作为参数传到测试用例函数中
@pytest.mark.parametrize('info',data) # 以数据驱动这个测试用例函数执行
def test_login(info,function_before):
    #test_login1
    #test_login2
    #test_login3
    u = info['username']
    p = info['password']
    exp = info['expected']
    assert exp == login(u,p)

def test_demo(function_before):
    # 使用夹具名称直接获取函数返回值
    print(function_before)
    assert 1 + 1 == 3

class TestUser:
    def test_user_1(self,function_before):
        pass
    def test_user_2(self,function_before):
        pass


