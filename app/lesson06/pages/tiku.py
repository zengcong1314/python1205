import time

from selenium.webdriver.common.by import By

from app.lesson06.common.base import BasePage


class tiku(BasePage):
    detail_tiku_locator = (By.XPATH, '//*[@text="Linux"]')
    title_locator = (By.XPATH, '//*[@resource-id = "com.lemon.lemonban:id/category_title"]')
    level_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/first_level"]')
    first_tiku_locator = (By.XPATH, '//*[@text="Linux--初级--第1套"]')
    header_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/toolbar_textview"]')

    def click_Linux(self):
        self.click_app(self.detail_tiku_locator)

    def click_level(self):
        # 点击初级
        self.click_app(self.level_locator)
        # 点击第一套题
        self.click_app(self.first_tiku_locator)
        return self

    def get_first_elem(self):
        # 第一个题得header
        title_first_elem = self.find_element(self.header_locator)
        return title_first_elem

    def swipe_random(self,i):
        # 滑动几次
        for i in range(i):
            self.swipe_left()
            time.sleep(1)
        return self

    def get_last_elem(self):
        # 获取后面的题
        title_last_elem = self.find_element(self.header_locator)
        return title_last_elem
