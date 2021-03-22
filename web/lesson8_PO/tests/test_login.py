"""
测试登录功能
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def get_driver():
    """启动浏览器"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
def login(driver,username,password):
    """登录过程"""
    driver.find_element(By.NAME, 'account').send_keys(username)
    driver.find_element(By.NAME, 'pass').send_keys(password)
    login_btn = driver.find_element(By.XPATH, "//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
    login_btn.click()

class TestLogin:
    def test_login_without_username_and_password(self):
        driver = get_driver()
        url = 'https://v4.ketangpai.com/User/login.html'
        driver.get(url)
        # 登录
        login_btn = driver.find_element(By.XPATH,"//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
        login_btn.click()
        expected = ['账号不能为空','密码不能为空']
        actual = driver.find_elements(By.CLASS_NAME,'error-tips')
        actual_value = [el.text for el in actual]
        assert expected == actual_value

    def test_login_without_username(self):
        driver = get_driver()
        url = 'https://v4.ketangpai.com/User/login.html'
        driver.get(url)
        # 输入用户名和密码
        driver.find_element(By.NAME,'account').send_keys('')
        driver.find_element(By.NAME,'pass').send_keys('1234')
        # login_pwd = driver.find_element(By.XPATH,"//input[@name='pass']")
        # login_pwd.send_keys('ABC_abc1')
        login_btn = driver.find_element(By.XPATH,"//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
        login_btn.click()
        expected = '账号不能为空'
        actual = driver.find_element(By.CLASS_NAME, 'error-tips')
        assert actual.text == expected

    def test_login_success(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        url = 'https://v4.ketangpai.com/User/login.html'
        driver.get(url)
        # 输入正确用户名和密码
        driver.find_element(By.NAME,'account').send_keys('looker53@sina.com')
        driver.find_element(By.NAME,'pass').send_keys('admin123456')
        login_btn = driver.find_element(By.XPATH,"//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
        login_btn.click()
        # 断言页面标题
        time.sleep(0.5)
        assert driver.current_url == 'https://v4.ketangpai.com/Main/index.html'
        user_elem = driver.find_element(By.CSS_SELECTOR,'.avatar') # By.XPATH //*[@class="avatar"]
        assert user_elem.get_attribute('title') == 'yuze'