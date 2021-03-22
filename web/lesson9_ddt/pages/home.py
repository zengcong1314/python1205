from selenium import webdriver

from selenium.webdriver.common.by import By

class HomePage():
    url = 'https://v4.ketangpai.com/Main/index.html'

    def __init__(self,driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)
        return self
    def get_username(self):
        """获取头像中的登陆用户名"""
        user_elem = self.driver.find_element(By.CSS_SELECTOR,'.avatar') # By.XPATH //*[@class="avatar"]
        return user_elem.get_attribute('title')