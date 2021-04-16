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

# toast 弹框定位文本,方法一：通过 text文本定位 toast弹框
text = '用户名或者密码不正确'
driver.find_element(By.XPATH,f'//*[contains(@text,"{text}")]')

# 方法二： //Android.widget.Toast
el = driver.find_element(By.XPATH,'//android.widget.Toast')
# 断言 获取文本 el.text