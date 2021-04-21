import time

from selenium.webdriver.common.by import By

from app.lesson06.common.base import BasePage
from app.lesson06.pages.nav import NavPage
from app.lesson06.pages.tiku import tiku
from app.project.data import  choose_topic
from app.project.pages.topic import TopicPage

def test_topic(login):

    driver = login
    # 点击题库按钮
    NavPage(driver).click_tiku()
    # 点击Linux题库
    tiku(driver).click_Linux()
    # 第一个断言，显示得文本是否是Linux
    actual = tiku(driver).find_element(tiku(driver).title_locator)
    assert 'Linux' == actual.text.strip()

    tiku(driver).click_level()
    title_first = int(tiku(driver).get_first_elem().text.split('/')[0])
    tiku(driver).swipe_random(5)
    title_last = int(tiku(driver).get_last_elem().text.split('/')[0])

    assert title_first + 5 == title_last

