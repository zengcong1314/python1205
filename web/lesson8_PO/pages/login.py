"""登录页面的 Page Object"""
from selenium.webdriver.common.by import By
class LoginPage:
    url = 'https://v4.ketangpai.com/User/login.html'

    def __init__(self,driver):
        self.driver = driver

    def login(self, username, password):
        """登录过程"""
        self.driver.find_element(By.NAME, 'account').send_keys(username)
        self.driver.find_element(By.NAME, 'pass').send_keys(password)
        login_btn = self.driver.find_element(By.XPATH, "//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
        login_btn.click()
        return self

    def load(self):
        """访问页面"""
        self.driver.get(self.url)
        return self

    # 还有其他的行为需要封装
    def clear(self):
        """清空用户名和密码"""
        self.driver.find_element(By.NAME, 'account').clear()
        self.driver.find_element(By.NAME, 'pass').clear()

    def get_error_msgs(self):
        """获取错误信息"""
        elem = self.driver.find_elements(By.CLASS_NAME,'error-tips')
        text = [el.text for el in elem]
        return text
