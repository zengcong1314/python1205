import time

import MB as MB
#from appium.webdriver import webdriver
from selenium.webdriver.android import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps["recreateChromeDriverSessions"] = True
desired_caps["automationName"] = "UiAutomator2"
desired_caps["deviceName"] = ""
desired_caps["appPackage"] = "com.tencent.mm"
desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
desired_caps["chromedriverExecutableDir"] = 'D:\chromedriver'
desired_caps["noReset"] = True
desired_caps["unicodeKeyboard"] = True

desired_caps["chromeOptions"] = {"androidProcess":"com.tencent.mm:appbrand0"}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
wait = WebDriverWait(driver,30)

# 主页的元素
loc = (MB.ID,'com.tencent.mm:id/baj')
wait.until(EC.visibility_of_all_elements_locates(loc))
time.sleep(3)
size = driver.get_window_size()
driver.swipe(size["width"]*0.5,size["height"]*0.2,size["width"]*0.5,size["height"]*0.9,100)

# 在下拉列表当中，点击 柠檬班软件测试 小程序
loc = (MB.A)