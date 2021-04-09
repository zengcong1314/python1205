import time
from appium.webdriver import Remote

class swipe:
    def __init__(self,driver,caps):

        # 创建一个会话
        self.driver = driver

    def swipe_left(self,offset=0.9):
        """封装swipe"""
        size = self.driver.get_window_size()
        height = size['height']
        width = size['width']
        time.sleep(3)
        self.driver.swipe(start_x=width * offset,
                     start_y=height * 0.5,
                     end_x=width * (1-offset),
                     end_y=height * 0.5)


    def swipe_right(self,offset=0.9):
        """封装swipe"""
        size = self.driver.get_window_size()
        height = size['height']
        width = size['width']
        time.sleep(3)
        self.driver.swipe(start_x=width * (1-offset),
                     start_y=height * 0.5,
                     end_x=width * offset,
                     end_y=height * 0.5)

    def swipe_up(self,offset=0.9):
        """封装swipe"""
        size = self.driver.get_window_size()
        height = size['height']
        width = size['width']
        time.sleep(3)
        self.driver.swipe(start_x=width * 0.5,
                     start_y=height * offset,
                     end_x=width * 0.5,
                     end_y=height * (1-offset))


    def swipe_down(self,offset=0.9):
        """封装swipe"""
        size = self.driver.get_window_size()
        height = size['height']
        width = size['width']
        time.sleep(3)
        self.driver.swipe(start_x=width * 0.5,
                     start_y=height * (1-offset),
                     end_x=width * 0.5,
                     end_y=height * offset)

if __name__ == '__main__':
    caps = {"platformName": "Android",
            "deviceName": "emulator-5554",
            # "app":r"E:\zengcong\software\appium\Future-release-2018.apk",
            "app": r"D:\software\Appium\Future-release-2018.apk",
            "noReset": True}

    driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                    desired_capabilities=caps)

    swipe(driver).swipe_left()

