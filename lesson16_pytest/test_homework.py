# 写一个登陆函数，输入用户名和密码，如果用户名='yuz' 并且 密码 = ‘123456’ 返回 ”登陆成功“，
# 否则返回”登陆失败“
# 编写测试用例函数，测试上面的登陆函数。至少 3 个测试用例。
# 使用 pytest 运行登陆成功用例。 （可以把运行的命令作为注释写在模块中）。
import pytest
def login(username,password):
    if username == 'yuz' and password == '123456':
        return "登录成功"
    else:
        return "登录失败"

@pytest.mark.success
def test_login_success():
    res = login('yuz','123456')
    expected = "登录成功"
    assert res == expected

def test_login_username_failure():
    res = login('zc','123456')
    expected = "登录失败"
    assert res == expected

def test_login_password_failure():
    res = login('yuz','12345')
    expected = "登录失败"
    assert res == expected

def test_login_username_Null():
    res = login('','123456')
    expected = "登录失败"
    assert res == expected

def test_login_password_Null():
    res = login('yuz','')
    expected = "登录失败"
    assert res == expected

#运行命令 pytest -m success