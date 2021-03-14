
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://www.baidu.com')

# 执行js 指令
js_code = 'return document'
driver.execute_script(js_code)

# 有哪一些指令在 selenium当中不存在的
# 1、
el = driver.find_element()
el.get_attribute('href')
