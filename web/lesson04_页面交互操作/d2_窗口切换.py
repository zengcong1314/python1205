import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

elem = driver.find_element('id','kw')

elem.send_keys('浩仔')
elem.submit()
time.sleep(2)
#  查找京东
driver.find_element_by_xpath('//*[@id="2"]/h3/a').click()
# 等待新页面出现
time.sleep(2)
# 切换窗口
# 窗口的句柄传进去 就是窗口的id
# 现在打开的所有的窗口句柄
print(driver.window_handles)
# 打印现在的窗口句柄
print(driver.current_window_handle)
driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)
print(driver.current_window_handle)
# 应该应答 京东
print(driver.title)
driver.quit()

