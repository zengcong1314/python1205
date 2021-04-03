import pytest
from selenium import webdriver
from web.lesson11_pre.pages.login import LoginPage


@pytest.fixture()
def get_driver():
    """启动浏览器"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def teacher_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.load().login("13925210746@163.com","admin123456")
    yield driver
    driver.quit()

@pytest.fixture()
def student_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.load().login("3403757034@qq.com","ABC_abc1")
    yield driver
    driver.quit()


