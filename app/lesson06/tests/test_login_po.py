from selenium.webdriver.common.by import By

from app.lesson06.pages.nav import NavPage
from app.lesson06.pages.user import UserPage
from app.project.common.base import BasePage

def test_login(driver):
    """测试步骤：app 当中按正常流程有没直接进入页面
    1、点击我的柠檬
    2、点击头像登录
    3、输入用户名和密码
    4、点击登录"""
    # 点击我的柠檬
    NavPage(driver).click_user()
    # 点击我的头像 
    UserPage(driver).login(username='',password='')
    # 断言 toast 弹框
    assert UserPage(driver).get_toast('手机号码或密码不能为空')