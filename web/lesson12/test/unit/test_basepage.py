import time

from selenium.webdriver import Chrome
from web.lesson11_pre.common.base import BasePage
class TestBasepage:
    def test_fill_method(self):
        driver = Chrome()
        d = BasePage(driver)
        # 从配置文件当中读取出来
        d.host = 'http://www.baidu.com'
        # 如果没有优化，每次访问某个页面时，都需要传入完整路径
        d.go_to('/')
        # 输入内容 搜索"紧挨孤独"
        d.fill(('id', 'kwyu'), '紧挨孤独')
        d.click(('id', 'su'))
        time.sleep(3)
        assert True

