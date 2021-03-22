import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from web.lesson8_PO.pages.login import LoginPage
from web.lesson8_PO.pages.home import HomePage


class TestLogin:
    def test_login_with_username(self,get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        actual_value = login_page.load().login('as', '').get_error_msgs()
        expected = '密码不能为空'
        assert actual_value[0] == expected

    def test_login_with_pwd(self,get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        actual_value = login_page.load().login('', 'asd').get_error_msgs()
        expected = '账号不能为空'
        assert actual_value[0] == expected

    def test_login_with_wrong_username(self,get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        actual_value = login_page.load().login('13403757034@qq.com', 'ABC_abc1').get_error_msgs()
        expected = '用户不存在'
        assert actual_value[0] == expected

    def test_login_with_wrong_pwd(self,get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        actual_value = login_page.load().login('3403757034@qq.com', 'ABC_abc12').get_error_msgs()
        expected = '密码错误, 你还可以尝试4次'
        assert actual_value[0] == expected

    def test_login_success(self,get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        actual_value = login_page.load().login('3403757034@qq.com', 'ABC_abc1').get_error_msgs()
        time.sleep(0.5)
        assert driver.current_url == home_page.url
        # 首页行为
        actual = home_page.get_username()
        assert actual == '曾聪'