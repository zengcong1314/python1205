from app.project.common.base import BasePage


def test_login(driver):
    """测试步骤：app 当中按正常流程有没直接进入页面
    1、点击我的柠檬
    2、点击头像登录
    3、输入用户名和密码
    4、点击登录"""
    page = BasePage(driver)
    driver.find_element().click()