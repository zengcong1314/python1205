import time
from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

caps = {"platformName":"Android",
        "deviceName":"emulator-5554",
        "appPackage":"com.lemon.lemonban",
        "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
        "chromedriverExecutable":'E:\zengcong\software\chromedriver\chromedriver_242.exe'
        }
# 创建一个会话
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=caps)
# 等待
driver.implicitly_wait(10)
# 获取现在的环境
print("现在的环境的原生界面",driver.current_context)
print("所有的环境",driver.contexts)
# 定位到师资团队的元素
driver.find_element(By.XPATH,'//*[@text="师资团队"]').click()

# 切换到 webview / h5 环境
driver.switch_to.context('WEBVIEW_com.lemon.lemonban')

# 获取现在的环境
print("现在的环境是h5界面",driver.current_context)
print("所有的环境",driver.contexts)

time.sleep(1)

# 我没有导入 selenium，
# 定位柠檬班几个字
driver.find_element(By.XPATH,'//*[text()="柠檬班"]').click()
# 回退主页
driver.back()
# 切回去原生页面
driver.switch_to.context('NATIVE_APP')