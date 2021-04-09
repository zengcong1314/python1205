import time
from appium.webdriver import Remote

def swipe_left(driver,offset=0.9):
    """封装swipe"""
    size = driver.get_window_size()
    height = size['height']
    width = size['width']
    time.sleep(3)
    driver.swipe(start_x=width * offset,
                 start_y=height * 0.5,
                 end_x=width * (1-offset),
                 end_y=height * 0.5)
    time.sleep(3)
    driver.swipe(start_x=width * 0.9,
                 start_y=height * 0.5,
                 end_x=width * 0.1,
                 end_y=height * 0.5)


def swipe_right(driver,offset=0.9):
    """封装swipe"""
    size = driver.get_window_size()
    height = size['height']
    width = size['width']
    time.sleep(3)
    driver.swipe(start_x=width * (1-offset),
                 start_y=height * 0.5,
                 end_x=width * offset,
                 end_y=height * 0.5)
    time.sleep(3)
    driver.swipe(start_x=width * 0.9,
                 start_y=height * 0.5,
                 end_x=width * 0.1,
                 end_y=height * 0.5)
def swipe_up(driver,offset=0.9):
    """封装swipe"""
    size = driver.get_window_size()
    height = size['height']
    width = size['width']
    time.sleep(3)
    driver.swipe(start_x=width * 0.5,
                 start_y=height * offset,
                 end_x=width * 0.5,
                 end_y=height * (1-offset))
    time.sleep(3)
    driver.swipe(start_x=width * 0.9,
                 start_y=height * 0.5,
                 end_x=width * 0.1,
                 end_y=height * 0.5)

caps = {"platformName":"Android",
        "deviceName":"emulator-5554",
        #"app":r"E:\zengcong\software\appium\Future-release-2018.apk",
        "app":r"D:\software\Appium\Future-release-2018.apk",
        "noReset": True}

# 创建一个会话
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=caps)

swipe_left(driver)
