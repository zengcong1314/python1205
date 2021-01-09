"""
写一个登陆函数，输入用户名和密码，如果用户名='yuz' 并且 密码 = ‘123456’ 返回 ”登陆成功“，
否则返回”登陆失败“
编写测试用例函数，测试上面的登陆函数。至少 3 个测试用例。
使用 pytest 运行登陆成功用例。 （可以把运行的命令作为注释写在模块中）。
"""

def login(username,password):
    """开发写的功能"""
    if username == 'yuz' and password == '123456':
        return "登录成功"
    else:
        return "登录失败"


def test_login_1():
    """第1个用例"""
    res = login('','')
    expected = "登录失败"
    assert res == expected

def test_login_2():
    res = login('zc','123456')
    expected = "登录失败"
    assert res == expected

def test_login_password_failure():
    res = login('yuz','12345')
    expected = "登录失败"
    assert res == expected

def test_login_3():
    res = login('yuz','123456')
    expected = "登录成功"
    assert res == expected

