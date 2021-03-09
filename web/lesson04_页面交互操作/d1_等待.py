import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
# 设置隐性等待 启动浏览器全局只需要设置一次 单位是s
# 隐性等待：只能用来等待元素出现
# driver.implicitly_wait(10)

driver.get("http://www.baidu.com")
# 把找元素替换成显性等待的方式
elem = driver.find_element("id","kw")

wait = WebDriverWait(driver,10)
# 元素定位的表达式 属性，属性值
# locator = ['id','kw']
locator = [By.ID,'kw']
# 等待某个元素加载
elem = wait.until(expected_conditions.presence_of_element_located(locator))
# 等待元素可见
elem = wait.until(expected_conditions.visibility_of_element_located(locator))
# 等待元素可以被点击
elem = wait.until(expected_conditions.element_to_be_clickable(locator))
elem.send_keys('浩仔')
elem.submit()
# 等待的条件：直到页面的标题当中包含“浩仔”
# wait....until....title_contains("浩仔")
# 时间超出了，就hi报错
# 显性等待一般可以被time.sleep 替换
wait = WebDriverWait(driver,timeout=10,poll_frequency=0.2)
wait.until(expected_conditions.title_contains('浩仔'))

print(driver.title)
driver.quit()
