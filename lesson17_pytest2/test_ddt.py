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

#只能实现一条用例
# def test_login():
#     """第一个用例"""
#     for case in data:
#         u = case["username"]
#         p = case["password"]
#         exp = case['expected']
#         assert exp == login(u,p)
#参数化过的测试用例
#数据驱动用法
@pytest.mark.parametrize('info',data) # 以数据驱动这个测试用例函数执行
def test_login(info):
    #test_login1
    #test_login2
    #test_login3
    u = info['username']
    p = info['password']
    exp = info['expected']
    assert exp == login(u,p)


