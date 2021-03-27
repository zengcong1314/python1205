import pytest
from selenium import webdriver

from web.lesson10_basepage.pages.login import LoginPage


@pytest.fixture()
def get_driver():
    """启动浏览器"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture()
def teacher_login(get_driver):
    login_page = LoginPage(get_driver)
    login_page.load().login("13925210746@163.com","admin123456")
    return get_driver


