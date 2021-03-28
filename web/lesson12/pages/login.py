"""登录页面的 Page Object"""
from selenium.webdriver.common.by import By

from web.lesson11_pre.common.base import BasePage
from web.lesson9_ddt.common.yaml_handler import yaml_config
from web.lesson9_ddt.locator import login_locator
host = yaml_config['host']

class LoginPage(BasePage):
    url = host + '/User/login.html'
    # 存放元素定位属性
    # 用户名
    username_locator = (By.NAME,'account')
    # 密码
    password_locator = (By.NAME, 'pass')
    # 登录按钮
    login_btn_locator = (By.XPATH, "//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
    # 错误信息弹框
    error_msg_locator = (By.CLASS_NAME, 'error-tips')

    def __init__(self,driver):
        self.driver = driver

    def login(self, username, password):
        """登录过程"""
        self.driver.find_element(*self.username_locator).send_keys(username)
        self.driver.find_element(*self.password_locator).send_keys(password)
        login_btn = self.driver.find_element(*self.login_btn_locator)
        login_btn.click()
        return self

    def load(self):
        """访问页面"""
        self.driver.get(self.url)
        return self

    # 还有其他的行为需要封装
    def clear(self):
        """清空用户名和密码"""
        self.driver.find_element(*self.username_locator).clear()
        self.driver.find_element(*self.password_locator).clear()

    def get_error_msgs(self):
        """获取错误信息"""
        elem = self.driver.find_elements(*self.error_msg_locator)
        text = [el.text for el in elem]
        return text
