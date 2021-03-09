import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('file:///D:/Project/python36/web/lesson04_%E9%A1%B5%E9%9D%A2%E4%BA%A4%E4%BA%92%E6%93%8D%E4%BD%9C/alert_demo.html')
h2 = driver.find_element('xpath','//h2')
h2.click()
time.sleep(2)

# 切换到alert，点击确定，switch_to.alert没有括号，也不需要传参数，因为全局只有一个
my_alert = driver.switch_to.alert
# 点击确定，回到主页面
my_alert.accept()
# 取消
my_alert.dismiss()
driver.find_element('xpath','//h2')

