import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.12306.cn/index/')

# 找到需要定位的元素 拷贝xpath的插件 chropath
el = driver.find_element('xpath',"//h2[contains(text(),'中国铁路官方微信')]")
time.sleep(2)
# 将元素滚动到可视范围之内
el.location_once_scrolled_into_view
time.sleep(3)
