
from selenium import webdriver
def test_start_selenium():
    # 测试步骤
    driver = webdriver.Chrome()
    url = 'http://www.baidu.com'
    driver.get(url)
    # 点点省略
    # 找到需要操作的元素
    input_el = driver.find_element('xpath','//*[@id="kw"]')
    driver.implicitly_wait(3)
    # 输入内容
    input_el.send_keys("你好，李焕英")
    #提交
    input_el.submit()
    driver.implicitly_wait(3)
    actual = driver.title
    print(driver.title)
    driver.quit()



    # 断言
    assert actual == '你好,李焕英_百度搜索'

# 怎么运行用例，怎么生成报告
# pytest
# pytest --html=output.html