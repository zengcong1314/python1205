
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.douban.com')
# 面试题：8种定位元素的方式
# driver.find_element_by_id()
# driver.find_element_by_class_name()
# driver.find_element_by_link_text()
# driver.find_element_by_name()
# driver.find_element_by_tag_name()
# driver.find_element_by_xpath()
# driver.find_element_by_css_selector()
# driver.find_element_by_partial_link_text()
#elem = driver.find_element_by_name('w')
'''
# elem 是一个叫做WebElement 的对象
print(elem)
# 对象是有属性的，对象有方法，对象的属性叫做实例属性，方法叫做实例方法
print(elem.send_keys('王者荣耀'))
# 输入框中的内容清空
elem.clear()
print(elem.parent)
# 获取元素的某个属性
print(elem.get_attribute('maxlength'))
'''


# 第二道：find_element 和find_elements有什么区别？
# find_element 得到一个webElement 对象
# s 得到的是一个列表
# find_element 只会返回查找到的第一个元素
# 如果找不到find_element 会报错NoSuchElementException，程序会停止运行
# s 会返回空列表
# 当我们想验证通过某个表达式能不能找到元素，判断页面中存不存在某个元素
if driver.find_elements_by_name('w'):
    # []
    print("元素存在")
else:
    print("元素不存在")

try:
    driver.find_element_by_name('w')
    print("元素存在")
except:
    print("元素不存在")
elems = driver.find_elements_by_name('w')
#print(elem)
print(elems)

# 自动化测试当中，不加 s 用的多。自动化测试中，要操作的元素一般是确定的，只会去点击其中的某一个，爬虫s 用得多，所有的元素抓起来，保存在一个地方
