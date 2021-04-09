import time

from appium.webdriver import Remote

# 得到一个driver对象
# 1、TODO: adb devices 确定手机在线
# 2、启动 appium 服务
# 如果appium 启动了4444 端口，就可以直接访问：因为 Remote 设置了默认参数
# Remote 提供的参数端口号和 appium 服务端口保持一致
# 平台，你要连接哪个手机，操作哪个app
# 三个变量 key 不能变的
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

"""
caps = {"platformName":"Android",
        "deviceName":"emulator-5554",
        "app":r"E:\zengcong\software\appium\lemon.apk"}
"""
caps = {"platformName":"Android",
        "deviceName":"emulator-5554",
        #"app":r"E:\zengcong\software\appium\Future-release-2018.apk",
        "app":r"D:\software\Appium\Future-release-2018.apk",
        "noReset": True}

# 创建一个会话
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=caps)

# 等待
driver.implicitly_wait(10)

# 进入首页看到欢迎界面，欢迎界面需要滑动
# driver.swipe(start_x=800,end_x=0,start_y=800,end_y=800)
# time.sleep(3)
# driver.swipe(start_x=800,end_x=0,start_y=800,end_y=800)
# time.sleep(3)

# 不能使用绝对坐标，得使用百分比坐标
# 获取屏幕的宽度和高度，800和1000，直接从x轴的90%，到10%
# 720PX ----> 80px,纵坐标：500 ----> 500
# 先获取屏幕的宽度和高度
size = driver.get_window_size()
print(size)
height = size['height']
width = size['width']
time.sleep(3)
driver.swipe(start_x=width * 0.9,
             start_y=height * 0.5,
             end_x=width * 0.1,
             end_y=height * 0.5)
time.sleep(3)
driver.swipe(start_x=width * 0.9,
             start_y=height * 0.5,
             end_x=width * 0.1,
             end_y=height * 0.5)
time.sleep(3)
