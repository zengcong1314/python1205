import pytest
from appium.webdriver import Remote
@pytest.fixture()
def driver():
    """启动和结束appium 对象"""
    caps = {"platformName": "Android",
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
    session.quit()