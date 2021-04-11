# 操作步骤
# 屏幕解锁
"""
action = TouchAction(d)
action.press().wait()
.move_to().wait()
.move_to().wait()
...
.move_to().release().perform()
"""


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

# 锁屏
driver.lock()
driver.back()
time.sleep(1)
# 解开屏幕
#driver.unlock()
time.sleep(1)
# 向上滑动
swipe_up(driver)
# 获取元素的属性
# el.rect	{"x":557,"y":252,"width":486,"height":486}

# 定位元素
el = driver.find_element(By.XPATH,'//*[@resource-id="com.android.systemui:id/lockPatternView"]')
# 第一个点
# rect = 	{"x":557,"y":252,"width":486,"height":486}
# 获取元素的x,y,width,height
rect = el.rect
start_x = rect['x']
start_y = rect['y']
width = rect['width']
height = rect['height']

point_01 = {'x': start_x + width * 1/6,'y': start_y + height * 1/6}
point_02 = {'x': start_x + width * 1/2,'y': start_y + height * 1/6}
point_03 = {'x': start_x + width * 5/6,'y': start_y + height * 1/6}
point_04 = {'x': start_x + width * 1/6,'y': start_y + height * 1/2}
point_05 = {'x': start_x + width * 1/2,'y': start_y + height * 1/2}
point_06 = {'x': start_x + width * 5/6,'y': start_y + height * 1/2}
point_07 = {'x': start_x + width * 1/6,'y': start_y + height * 5/6}
point_08 = {'x': start_x + width * 1/2,'y': start_y + height * 5/6}
point_09 = {'x': start_x + width * 5/6,'y': start_y + height * 5/6}

# 调用 touchAction
action = TouchAction(driver)
# action.press(x=point_01['x'],y=point_01['y'])
action.press(**point_01).wait(200).\
    move_to(**point_02).wait(200).\
    move_to(**point_03).wait(200).\
    move_to(**point_05).wait(200).\
    move_to(**point_07).wait(200).\
    move_to(**point_08).wait(200).\
    move_to(**point_09).wait(200).\
    release().perform()

time.sleep(1)


