import time

from selenium.webdriver.common.by import By


class TopicPage:
    topic_btn = (By.XPATH,'//*[@resource-id="com.lemon.lemonban:id/navigation_tiku"]')
    linux = (By.XPATH,'//*[@text="Linux"]')

    def __init__(self,driver):
        self.driver = driver

    def topic(self):
        self.driver.find_element(*self.topic_btn).click()

    def get_class(self,name):
        # 根据课程名称定位元素 f'//*[text()="{name}"]','//*[text()={}]'.format(name)
        el = self.driver.find_element(By.XPATH, f'//*[@text="{name}"]')
        time.sleep(2)
        return el



