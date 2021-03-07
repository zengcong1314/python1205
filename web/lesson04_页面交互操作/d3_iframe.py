"""iframe 内嵌网页"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.w3school.com.cn/tiy/t.asp?f=html_select')

# 如果想找一个iframe 当中的元素，不能直接查找，而是先要进入iframe当中
# 提供iframe 的标识：index(一般不用，在页面很难确定层级)，name,iframe Webelement
iframe = driver.find_element('id','iframeResult')
driver.switch_to.frame(iframe)
#driver.switch_to.frame('iframeResult')
elem = driver.find_element_by_xpath('//select')
print(elem)


