"""
键盘操作
按回车键提交
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://www.baidu.com')
input = driver.find_element('id','kw')
input.send_keys('哈哈')

# 方式一：找到百度一下这个按钮，点击元素(通用)
# 方式二：
# 如果该元素不在form 表单下，还能通过这种方式提交吗？不能 源码通过form表单
input.submit()

# 方式三：触发键盘上的 回车键
input.send_keys(Keys.ENTER)

# send_keys 支持不定长参数，可以触发多个动作
input.send_keys(Keys.CONTROL,'a')  # control + a
input.send_keys(Keys.CONTROL,Keys.SPACE)  # control + 空格

# 全局执行，传键盘操作
ac = ActionChains(driver)
ac.send_keys(Keys.ENTER).perform()