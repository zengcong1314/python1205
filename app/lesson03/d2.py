from appium.webdriver import Remote

# 得到一个driver对象
# 1、TODO: adb devices 确定手机在线
# 2、启动 appium 服务
# 如果appium 启动了4444 端口，就可以直接访问：因为 Remote 设置了默认参数
# Remote 提供的参数端口号和 appium 服务端口保持一致
# 平台，你要连接哪个手机，操作哪个app
# 三个变量 key 不能变的
from selenium.webdriver.common.by import By

"""
caps = {"platformName":"Android",
        "deviceName":"emulator-5554",
        "app":r"E:\zengcong\software\appium\lemon.apk"}
"""
caps = {"platformName":"Android",
        # 校验系统版本
        # "platformVersion":"8.0",
        "automationName":"Uiautomator2",
        "deviceName":"emulator-5554",
        #"app":r"E:\zengcong\software\appium\Future-release-2018.apk",
        "appPackage":"com.lemon.lemonban",
        "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
        # 重启设置，会使用缓存数据
        "noReset": True}

# 创建一个会话
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=caps)
# 等待
driver.implicitly_wait(10)
# 查找元素
driver.find_element('id')
driver.find_element('xpath')
# 这是通过安卓原生的定位方式，我们需要写Java 语言，没有提示
# 
locator = 'new UiSelector().resourceId("com.lemon.lemonban:id/navigation_my").checkable(false)'
driver.find_element_by_android_uiautomator(locator)

# tagname 不行
# class_name,可以，但是相当于原来的 tag_name,不能精确定位
#