import time
from appium.webdriver import Remote

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.size = driver.get_window_size()
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