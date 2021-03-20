import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login_with_username(self):
        driver = webdriver.Chrome()
        url = 'https://v4.ketangpai.com/User/login.html'
        driver.get(url)
        login_username = driver.find_element(By.XPATH,"//input[@name='account']")
        login_username.send_keys('3403757034@qq.com')
        login_btn = driver.find_element(By.XPATH,"//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
        login_btn.click()
        expected = '密码不能为空'
        actual = driver.find_elements(By.CLASS_NAME, 'error-tips')
        assert actual[0].text == expected

    def test_login_with_pwd(self):
        driver = webdriver.Chrome()
        url = 'https://v4.ketangpai.com/User/login.html'
        driver.get(url)

        login_pwd = driver.find_element(By.XPATH,"//input[@name='pass']")
        login_pwd.send_keys('ABC_abc1')
        login_btn = driver.find_element(By.XPATH,"//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
        login_btn.click()

        expected = '账号不能为空'
        actual = driver.find_elements(By.CLASS_NAME, 'error-tips')
        assert actual[0].text == expected

    def test_login_with_wrong_username(self):
        driver = webdriver.Chrome()
        url = 'https://v4.ketangpai.com/User/login.html'
        driver.get(url)
        login_username = driver.find_element(By.XPATH,"//input[@name='account']")
        login_username.send_keys('13403757034@qq.com')
        login_pwd = driver.find_element(By.XPATH,"//input[@name='pass']")
        login_pwd.send_keys('ABC_abc1')
        login_btn = driver.find_element(By.XPATH,"//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
        login_btn.click()
        time.sleep(2)
        expected = '用户不存在'
        actual = driver.find_elements(By.CLASS_NAME, 'error-tips')
        assert actual[0].text == expected

    def test_login_with_wrong_pwd(self):
        driver = webdriver.Chrome()
        url = 'https://v4.ketangpai.com/User/login.html'
        driver.get(url)
        login_username = driver.find_element(By.XPATH,"//input[@name='account']")
        login_username.send_keys('3403757034@qq.com')
        login_pwd = driver.find_element(By.XPATH,"//input[@name='pass']")
        login_pwd.send_keys('ABC_abc12')
        login_btn = driver.find_element(By.XPATH,"//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
        login_btn.click()
        time.sleep(2)
        expected = '密码错误, 你还可以尝试4次'
        actual = driver.find_elements(By.CLASS_NAME, 'error-tips')
        assert actual[0].text == expected

    def test_login_success(self):
        driver = webdriver.Chrome()
        url = 'https://v4.ketangpai.com/User/login.html'
        driver.get(url)
        login_username = driver.find_element(By.XPATH,"//input[@name='account']")
        login_username.send_keys('3403757034@qq.com')
        login_pwd = driver.find_element(By.XPATH,"//input[@name='pass']")
        login_pwd.send_keys('ABC_abc1')
        login_btn = driver.find_element(By.XPATH,"//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
        login_btn.click()
        time.sleep(2)
        expected = ''
        actual = driver.find_elements(By.XPATH, '//img[@title="曾聪"]')
        assert actual[0].text == expected