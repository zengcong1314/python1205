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

# 按下物理按键
driver.press_keycode()

