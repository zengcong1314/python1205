import time

from selenium.webdriver.common.by import By

from app.lesson06.common.base import BasePage
from app.project.data import  choose_topic
from app.project.pages.topic import TopicPage

def test_topic(login):
    """
    测试步骤：
    1、登陆成功
    2、点击题库按钮
    3、点击Linux 题库
    4、断言标题
    5、点击初级
    6、获取第一道题的 title
    7、滑动
    8、获取后面题目的 title
    9、断言： last_title - first_title = 滑动的次数
    :param login:
    :return:
    """
    driver = login
    basepage = BasePage(driver)
    # 点击题库按钮
    tiku_locator = (By.XPATH,'//*[@resource-id="com.lemon.lemonban:id/navigation_tiku"]')
    basepage.click_app(tiku_locator)
    # 点击Linux题库
    detail_tiku_locator = (By.XPATH,'//*[@text="Linux"]')
    basepage.click_app(detail_tiku_locator)
    # 第一个断言，显示得文本是否是Linux
    title_locator = (By.XPATH,'//*[@resource-id = "com.lemon.lemonban:id/category_title"]')
    actual = basepage.find_element(title_locator)
    assert 'Linux' == actual.text.strip()

    # 点击初级
    level_locator = (By.XPATH,'//*[@resource-id="com.lemon.lemonban:id/first_level"]')
    basepage.click_app(level_locator)

    # 点击第一套提
    first_tiku_locator = (By.XPATH,'//*[@text="Linux--初级--第1套"]')
    basepage.click_app(first_tiku_locator)

    # 第一个题得header
    header_locator = (By.XPATH,'//*[@resource-id="com.lemon.lemonban:id/toolbar_textview"]')
    title_first_elem = basepage.find_element(header_locator)
    title_first = int(title_first_elem.text.split('/')[0])

    # 滑动几次
    for i in range(5):
        basepage.swipe_left()
        time.sleep(1)

    # 获取后面的题
    title_last_elem = basepage.find_element(header_locator)
    title_last = int(title_last_elem.text.split('/')[0])
    assert title_first + 5 == title_last

