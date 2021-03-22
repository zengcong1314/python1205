"""
测试登录功能
"""
import time

import pytest
from web.lesson9_ddt.pages.login import LoginPage
from web.lesson9_ddt.pages.home import HomePage
from web.lesson9_ddt.data import login

class TestLogin:
    @pytest.mark.parametrize('info', login.without_username_pwd)
    def test_login_without_username_and_password(self,get_driver,info):
        username, password, expected = info
        driver = get_driver
        login_page = LoginPage(driver)
        actual_value = login_page.load().login(username,password).get_error_msgs()
        assert expected[0] == actual_value[0]
        assert expected[1] == actual_value[1]

    @pytest.mark.parametrize('info',login.without_username)
    def test_login_without_username_or_pwd(self,get_driver,info):
        username, password, expected = info
        driver = get_driver
        login_page = LoginPage(driver)
        actual_value = login_page.load().login(username, password).get_error_msgs()
        assert actual_value[0] == expected

    @pytest.mark.parametrize('info',login.success)
    def test_login_student_success(self,get_driver,info):
        username,password,expected = info
        driver = get_driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        login_page.load()
        login_page.login(username, password)
        time.sleep(0.5)
        assert driver.current_url == home_page.url
        actual = home_page.get_username()
        assert actual == expected

