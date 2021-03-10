"""iframe 内嵌网页"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.w3school.com.cn/tiy/t.asp?f=html_select')

# 如果想找一个iframe 当中的元素，不能直接查找，而是先要进入iframe当中
# 提供iframe 的标识：index(一般不用，在页面很难确定层级)，name,iframe Webelement

# 通过 WebElement 切换
iframe = driver.find_element('id','iframeResult')
# driver.switch_to.frame(iframe)

# 等待 iframe 切换成功
WebDriverWait(driver,5).until(expected_conditions.frame_to_be_available_and_switch_to_it(iframe))
# iframe 切换只要等待了，不需要切换，自动完成切换
"""
# 通过name属性切换
driver.switch_to.frame('iframeResult')

# 通过索引切换
driver.switch_to.frame(0)
"""

elem = driver.find_element('xpath','//select')

# 退回主页面
driver.switch_to.default_content()

# 退回父级iframe
# driver.switch_to.parent_frame()
print(elem)


