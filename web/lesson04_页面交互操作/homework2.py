"""
作业二：  https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable， 通过代码完成该网址的鼠标拖拽动作
"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
wait = WebDriverWait(driver,timeout=10)
wait.until(expected_conditions.title_contains('菜鸟教程'))
# 复杂版
# 初始化 ActionChains:动作链条
action = ActionChains(driver)
# 切换iframe
iframe = driver.find_element('id','iframeResult')
driver.switch_to.frame(iframe)
# 定位一个元素
start = driver.find_element('xpath',"//div[@id='draggable']")
end = driver.find_element('xpath',"//div[@id='droppable']")
# 拖拽操作
action.drag_and_drop(start,end).perform()
time.sleep(2)

driver.quit()