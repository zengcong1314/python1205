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
# 找元素
driver.find_element(By.ID,'com.lemon.lemonban:id/navigation_my').click()

driver.quit()

# 可以不提供 app路径，而是提供 app 的包名 和 activity
# 包名：app 在你手机上的ID
# activity： app 当中的哪个页面。
# 查看 app name activity 命令：aapt dump badging E:\zengcong\software\appium\lemon.apk
# 这个要先安装包
