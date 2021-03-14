"""select"""
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("file:///D:/zengcong/py37/web/lesson05_UI操作/select.html")

# 点击zc
"""
# 第一种方式选择option元素
driver.find_element('xpath','//option[text()="zc"]').click()
time.sleep(2)
"""

# 另外封装的一种方式
# 先找到select 元素，再把元素对象传入Select 类
s = driver.find_element('id','myselect')
s_obj = Select(s)
s_obj.select_by_visible_text('zc')
# option value 属性选择
s_obj.select_by_value('z')
# 通过索引
s_obj.select_by_index(2)
time.sleep(2)