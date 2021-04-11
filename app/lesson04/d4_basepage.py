import time
from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.size = driver.get_window_sizt()
        self.height = self.size['height']
        self.width = self.size['width']

    def swipe_left(self, offset=0.9):
        """封装swipe"""

        self.driver.swipe(start_x=self.width * offset,
                          start_y=self.height * 0.5,
                          end_x=self.width * (1 - offset),
                          end_y=self.height * 0.5)

    def swipe_right(self, offset=0.9):
        """封装swipe"""
        self.driver.swipe(start_x=self.width * (1 - offset),
                          start_y=self.height * 0.5,
                          end_x=self.width * offset,
                          end_y=self.height * 0.5)

    def swipe_up(self, offset=0.9):
        """封装swipe"""
        self.driver.swipe(start_x=self.width * 0.5,
                          start_y=self.height * offset,
                          end_x=self.width * 0.5,
                          end_y=self.height * (1 - offset))

    def swipe_down(self, offset=0.9):
        """封装swipe"""
        self.driver.swipe(start_x=self.width * 0.5,
                          start_y=self.height * (1 - offset),
                          end_x=self.width * 0.5,
                          end_y=self.height * offset)

    def swipe1(self,direct='left',offset=0.9):
        if direct == 'left':
            return self.swipe_left(offset)
        elif direct == 'right':
            return self.swipe_right(offset)
        elif direct == 'up':
            return self.swipe_up(offset)
        else:
            return self.swipe_down(offset)

    def sudoku(self,driver):
        driver.lock()
        driver.back()
        time.sleep(1)
        self.swipe_up(driver)
        el = driver.find_element(By.XPATH, '//*[@resource-id="com.android.systemui:id/lockPatternView"]')
        rect = el.rect
        start_x = rect['x']
        start_y = rect['y']
        width = rect['width']
        height = rect['height']

        point_01 = {'x': start_x + width * 1 / 6, 'y': start_y + height * 1 / 6}
        point_02 = {'x': start_x + width * 1 / 2, 'y': start_y + height * 1 / 6}
        point_03 = {'x': start_x + width * 5 / 6, 'y': start_y + height * 1 / 6}
        point_04 = {'x': start_x + width * 1 / 6, 'y': start_y + height * 1 / 2}
        point_05 = {'x': start_x + width * 1 / 2, 'y': start_y + height * 1 / 2}
        point_06 = {'x': start_x + width * 5 / 6, 'y': start_y + height * 1 / 2}
        point_07 = {'x': start_x + width * 1 / 6, 'y': start_y + height * 5 / 6}
        point_08 = {'x': start_x + width * 1 / 2, 'y': start_y + height * 5 / 6}
        point_09 = {'x': start_x + width * 5 / 6, 'y': start_y + height * 5 / 6}

        action = TouchAction(driver)
        action.press(**point_01).wait(200). \
            move_to(**point_02).wait(200). \
            move_to(**point_03).wait(200). \
            move_to(**point_05).wait(200). \
            move_to(**point_07).wait(200). \
            move_to(**point_08).wait(200). \
            move_to(**point_09).wait(200). \
            release().perform()