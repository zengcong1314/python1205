"""python自动化"""
import time

from web.lesson10_basepage.pages.home_ba import HomePage
from web.lesson10_basepage.common import helper




class TestAddClass:
    def test_add_success(self,teacher_login):
        # 获取浏览器
        driver = teacher_login
        # 进入首页
        home_page = HomePage(driver)
        # 添加课程
        class_name = helper.gen_class_name()
        home_page.add_class(class_name,term="2011-2012")
        time.sleep(2)
        # 断言
        assert home_page.get_class(class_name)

