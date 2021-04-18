from selenium.webdriver.common.by import By

from app.lesson06.common.base import BasePage
class UserPage(BasePage):

    avatar_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/fragment_my_lemon_avatar_layout"]')
    mobile_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/et_mobile"]')
    pwd_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/et_password"]')
    login_btn_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/content"]/android.widget.FrameLayout[1]')

    def login(self,username,password):
        self.click_app(self.avatar_locator)
        # 输入用户名
        self.fill(self.mobile_locator, username)
        # 输入密码
        self.fill(self.pwd_locator, password)
        # 点击登录
        self.click_app(self.login_btn_locator)