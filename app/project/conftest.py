import pytest
from appium.webdriver import Remote

from app.project.pages.login import LoginPage


@pytest.fixture()
def driver():
    """启动和结束appium 对象"""
    caps = {"platformName": "Android",
            "automationName":"Uiautomator2", # 使用toast弹框必须要使用uiautomator2 才能定位
            "deviceName": "emulator-5554",
            "appPackage": "com.lemon.lemonban",
            "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"
            }
    # 创建一个会话
    session = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                    desired_capabilities=caps)
    # 等待
    session.implicitly_wait(10)
    yield session
    #session.quit()

@pytest.fixture()
def login(driver):
    session = driver
    login_page = LoginPage(session)
    login_page.login("13925210746","210746")
    yield session
    session.quit()

