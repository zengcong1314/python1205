import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.12306.cn/index/')

# 执行 JS 语句写上日期
time.sleep(5)
js_code = "let input = document.getElementById('train_date');input.readOnly=false;input.value='2021-03-11'"
driver.execute_script(js_code)
time.sleep(5)

# 可以把 python和JS 混用
input_element = driver.find_element('id','train_date')
js_code = "input.readOnly=false;input.value='2021-03-11'"



