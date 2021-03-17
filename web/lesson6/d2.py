import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.12306.cn/index/')

# 日期框的操作
# 执行 JS 语句写上日期
# time.sleep(5)
# js_code = "let input = document.getElementById('train_date');input.readOnly=false;input.value='2021-03-11'"
# driver.execute_script(js_code)
# time.sleep(5)

# 可以把 python和JS 混用
input_element = driver.find_element('id','train_date')
time.sleep(3)
# 变量有多个，可以用arguments[1] ，execute_script(js_code,input_element，input_element1)
js_code = "arguments[0].readOnly=false;arguments[0].value='2021-03-11'"
driver.execute_script(js_code,input_element)

time.sleep(3)


# 窗口滚动 懒加载
# scrollTo scrollBy


