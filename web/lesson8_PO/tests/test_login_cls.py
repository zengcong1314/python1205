"""
测试登录功能
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from web.lesson8_PO.pages.login import LoginPage
from web.lesson8_PO.pages.home import HomePage

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

    def test_login_without_username(self,get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        actual_value = login_page.load().login('', 'as').get_error_msgs()
        expected = '账号不能为空'
        assert actual_value[0] == expected

    def test_login_success(self,get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        # 访问url
        login_page.load()
        login_page.login('looker53@sina.com', 'admin123456')

        # 断言页面标题
        time.sleep(0.5)
        assert driver.current_url == home_page.url
        # 首页行为
        actual = home_page.get_username()
        assert actual == 'yuze'
