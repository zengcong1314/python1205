import time

from selenium import webdriver

driver = webdriver.Chrome()
# 设置隐性等待 启动浏览器全局只需要设置一次 单位是s
# 隐性等待：只能用来等待元素出现
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")
elem = driver.find_element("id","kw")
elem.send_keys('浩仔')
elem.submit()
# 强制等待
time.sleep(2)

print(driver.title)
driver.quit()

# 显性等待
# xpath
# 三种等待