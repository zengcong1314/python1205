"""
测试登录功能
"""
import time

import pytest
from web.lesson9_ddt.pages.login import LoginPage
from web.lesson9_ddt.pages.home import HomePage
from web.lesson9_ddt.data import login

class TestLogin:
    def test_login_without_username_and_password(self,get_driver):
        # 在测试用例函数中接收fixture 中的返回值，不需要加括号
        # 初始化页面对象
        driver = get_driver
        login_page = LoginPage(driver)

        # 获取实际结果
        actual_value = login_page.load().login('','').get_error_msgs()
        #login_page.load(url)
        """
        # 登录
        login_page.login(driver,'','')
        # 获取错误信息
        actual_value = login_page.get_error_msgs()
        """
        # 断言
        expected = ['账号不能为空', '密码不能为空']
        assert expected == actual_value
    @pytest.mark.parametrize('info',[('','ab','账号不能为空')])
    def test_login_without_username(self,get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        actual_value = login_page.load().login('', 'as').get_error_msgs()
        expected = '账号不能为空'
        assert actual_value[0] == expected

    @pytest.mark.parametrize('info',login.success)
    def test_login_student_success(self,get_driver,info):
        username,password,expected = info
        driver = get_driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        # 访问url
        login_page.load()
        login_page.login(username, password)

        # 断言页面标题
        time.sleep(0.5)
        assert driver.current_url == home_page.url
        # 首页行为
        actual = home_page.get_username()
        assert actual == expected

    # def test_login_teacher_success(self,get_driver):
    #     driver = get_driver
    #     login_page = LoginPage(driver)
    #     home_page = HomePage(driver)
    #     # 访问url
    #     login_page.load()
    #     login_page.login('wagyu1016@163.com', 'admin123456')
    #
    #     # 断言页面标题
    #     time.sleep(0.5)
    #     assert driver.current_url == home_page.url
    #     # 首页行为
    #     actual = home_page.get_username()
    #     assert actual == 'wagyu'
