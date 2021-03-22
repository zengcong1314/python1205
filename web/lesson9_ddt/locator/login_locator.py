# 存放元素定位属性
# 用户名
from selenium.webdriver.common.by import By

username_locator = (By.NAME, 'account')
# 密码
password_locator = (By.NAME, 'pass')
# 登录按钮
login_btn_locator = (By.XPATH, "//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
# 错误信息弹框
error_msg_locator = (By.CLASS_NAME, 'error-tips')