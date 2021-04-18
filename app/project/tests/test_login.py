from selenium.webdriver.common.by import By

from app.project.common.base import BasePage

def test_login(driver):
    """测试步骤：app 当中按正常流程有没直接进入页面
    1、点击我的柠檬
    2、点击头像登录
    3、输入用户名和密码
    4、点击登录"""
    page = BasePage(driver)
    #driver.find_element().click()
    # 点击我的柠檬 //*[@resource-id="com.lemon.lemonban:id/navigation_my"]
    my_locator = (By.XPATH,'//*[@resource-id="com.lemon.lemonban:id/navigation_my"]')
    page.click_app(my_locator)
    # 点击我的头像 //*[@resource-id="com.lemon.lemonban:id/fragment_my_lemon_avatar_layout"]
    avatar_locator = (By.XPATH,'//*[@resource-id="com.lemon.lemonban:id/fragment_my_lemon_avatar_layout"]')
    page.click_app(avatar_locator)
    # 输入用户名 //*[@resource-id="com.lemon.lemonban:id/et_mobile"]
    mobile_locator = (By.XPATH,'//*[@resource-id="com.lemon.lemonban:id/et_mobile"]')
    page.fill(mobile_locator,'')
    # 输入密码
    pwd_locator = (By.XPATH,'//*[@resource-id="com.lemon.lemonban:id/et_password"]')
    page.fill(pwd_locator,'')
    # 点击登录  //*[@resource-id="com.lemon.lemonban:id/content"]/android.widget.FrameLayout[1]
    login_btn_locator = (By.XPATH,'//*[@resource-id="com.lemon.lemonban:id/content"]/android.widget.FrameLayout[1]')
    page.click_app(login_btn_locator)

    # 断言 toast 弹框
    assert page.get_toast('手机号码或密码不能为空')