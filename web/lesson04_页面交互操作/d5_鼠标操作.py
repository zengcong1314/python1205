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
elem = driver.find_element('xpath',"//span[@id='s-usersetting-top']")
# click操作
action.click(elem).perform()
time.sleep(5)

# 简单版
# h2 = driver.find_element('xpath','//h2')
# h2.click()


