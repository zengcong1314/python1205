from selenium.webdriver.common.by import By

from app.lesson06.common.base import BasePage


class NavPage(BasePage):
    my_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/navigation_my"]')
    tiku_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/navigation_tiku"]')
    def click_home(self):
        pass

    def click_tiku(self):
        self.click_app(self.tiku_locator)
        return self

    def click_user(self):
        self.click_app(self.my_locator)
        # 返回 self 方便链式调用
        return self

