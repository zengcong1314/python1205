import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

elem = driver.find_element('id','kw')

elem.send_keys('浩仔')
elem.submit()

all_handles = driver.window_handles
#  查找京东
driver.find_element_by_xpath('//*[@id="2"]/h3/a').click()
"""
# 等待新页面出现
time.sleep(2)
# 切换窗口
# 窗口的句柄传进去 就是窗口的id
# 现在打开的所有的窗口句柄
print(driver.window_handles)
# 打印现在的窗口句柄
print(driver.current_window_handle)
driver.switch_to.window(driver.window_handles[-1])
# 万一窗口没切过来（需要时间加载）得到的title还是原来的，一般来说，加载新窗口是非常快
time.sleep(2)
print(driver.current_window_handle)
# 应该应答 京东
"""

# 显性的等待，等待新窗口出现
wait = WebDriverWait(driver,2)
wait.until(expected_conditions.new_window_is_opened(all_handles))
print(driver.title)
driver.quit()

