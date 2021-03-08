"""
1，进入百度
2，输入柠檬班
3，定位柠檬班腾讯课堂，点击进入
4，定位腾讯课堂页面的任意元素。
注意：所有元素定位练习显性等待的用法。
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# 全局隐式等待
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')
elem = driver.find_element('id','kw')
elem.send_keys('柠檬班')
elem.submit()
# 显示等待
wait = WebDriverWait(driver,timeout=10)
wait.until(expected_conditions.title_contains('柠檬班'))
# 查看柠檬班腾讯课堂
driver.find_element('xpath','//*[@id="1"]/h3/a').click()
# 强制等待
# time.sleep(3)

# 切换窗口
driver.switch_to.window(driver.window_handles[-1])
# 显示等待
wait = WebDriverWait(driver,timeout=10)
wait.until(expected_conditions.title_contains('腾讯课堂官网'))

# 定位轮询图片
img = driver.find_element('xpath',"//li[@class='agency-big-banner-li current']")
# 定位主页
elem2 = driver.find_element('xpath',"//h2[text()='主页']")

driver.quit()
# 定位刷刷你们的工资单
# //h4[text()='刷新你们的工资单']
# 课程 软件测试之python全栈自动化测试工程师第38期【柠檬班VIP】
# //a[@href='https://ke.qq.com/course/325554?quicklink=1']
# //span[contains(text(),'软件测试从零开始')]
# 定位图片//div[@class='rec-group-mask']




