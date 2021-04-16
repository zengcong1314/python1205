from appium.webdriver.common.multi_action import MultiAction
import time
from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

caps = {"platformName":"Android",
        "deviceName":"emulator-5554",
        "appPackage":"com.lemon.lemonban",
        "appActivity":"com.lemon.lemonban.activity.WelcomeActivity"
        }
# 创建一个会话
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=caps)
# 等待
driver.implicitly_wait(10)
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.size = driver.get_window_sizt()
        self.height = self.size['height']
        self.width = self.size['width']

    def zoom(self,offset):
        """放大"""
        action_1 = TouchAction(self.driver)
        action_1.press(x=self.width / 2,y=self.height / 2).move_to(x=self.width / 2,y=self.height / 2 - offset).release()
        action_2 = TouchAction(self.driver)
        action_2.press(x=self.width / 2,y=self.height / 2).move_to(x=self.width / 2,y=self.height / 2 + offset).release()
        m = MultiAction(self.driver)
        m.add(action_1,action_2)
        m.perform()

    def pinch(self,offset):
        """缩小"""
        action_1 = TouchAction(self.driver)
        action_1.press(x=self.width / 2,y=self.height / 2 - offset).move_to(x=self.width / 2,y=self.height / 2).release()
        action_2 = TouchAction(self.driver)
        action_2.press(x=self.width / 2,y=self.height / 2 + offset).move_to(x=self.width / 2,y=self.height / 2).release()
        m = MultiAction(self.driver)
        m.add(action_1,action_2)
        m.perform()


# a1 = TouchAction(driver)
# a2 = TouchAction(driver)
# a1.press().move_to().release()
# a2.press().move_to().release()
# MultiAction(driver).add(a1,a2).perform()