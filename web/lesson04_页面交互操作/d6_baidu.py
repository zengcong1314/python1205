import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 复杂版
# 初始化 ActionChains:动作链条
action = ActionChains(driver)
# 定位一个元素
setting = driver.find_element('xpath',"//span[@id='s-usersetting-top']")
# 鼠标悬停，move_to_element
action.move_to_element(setting).perform()
time.sleep(5)

# 简单版
# h2 = driver.find_element('xpath','//h2')
# h2.click()

# 找到高级搜索
adv_setting = driver.find_element('xpath',"//a[text()='高级搜索']")
time.sleep(2)
adv_setting.click()
time.sleep(2)

# 连续操作 context_click 右击  drag_and_drop() 拖拽 链式调用
action.move_to_element(setting).click(adv_setting).drag_and_drop().context_click().perform()
action.double_click()