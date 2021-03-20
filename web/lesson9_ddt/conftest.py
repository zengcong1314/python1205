import pytest
from selenium import webdriver

@pytest.fixture()
def get_driver():
    """启动浏览器"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

