import time

from selenium.webdriver import ActionChains,Chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    host = ''
    def __init__(self,driver: Chrome):
        self.driver = driver


    def go_to(self,url):
        """访问页面"""
        if url.startswith('http'):
            self.driver.get(url)
        else:
            url = self.host + url
            self.driver.get(url)
        return self

    def click(self,locator: tuple,force=False):
        """点击"""
        el = self.driver.find_element(*locator)
        # 有时候，当元素不可点击的时候，使用el.click 不生效
        if not force:
            self.driver.execute_script("arguments[0].click()", el)
        else:
            self.driver.execute_script("arguments[0].click({force:true})", el)
        return self

    def fill(self,locator,text):
        """输入内容"""
        el = self.driver.find_element(*locator)
        el.send_keys(text)
        return self

    def get_attribute(self,locator,attr_name):
        """获取元素属性"""
        elem = self.driver.find_element(*locator)
        return  elem.get_attribute(attr_name)

    # el.name el.href
    # 把方法变成属性，调用时可以不加括号
    @property
    def name(self,locator):
        # 获取元素的name属性
        return self.get_attribute(locator,'name')

# if __name__ == '__main__':
    # el.name
    # el.get_attribute('name')

    def double_click(self,locator):
        """双击"""
        el = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.double_click(el).perform()
        return self

    # 鼠标拖动，鼠标悬停
    def drag_and_drop(self,start_locator,end_locator):
        elem_start = self.driver.find_element(*start_locator)
        elem_end = self.driver.find_element(*end_locator)
        action = ActionChains(self.driver)
        action.double_click(elem_start,elem_end).perform()
        return self

    def hover(self,locator):
        """鼠标悬停"""
        el = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.move_to_element(el).perform()
        return self

    def wait_visible(self,locator,timeout=10,poll=0.2):
        """等待元素可见"""
        wait = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll)
        el = wait.until(expected_conditions.invisibility_of_element_located(locator))
        return el

    def wait_presence(self,locator,timeout=10,poll=0.2):
        """等待元素加载"""
        wait = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll)
        el = wait.until(expected_conditions.presence_of_element_located(locator))
        return  el

    def wait_clickable(self,locator,timeout=10,poll=0.2):
        """等待元素可以被点击"""
        wait = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll)
        el = wait.until(expected_conditions.element_to_be_clickable(locator))
        return  el

    def switch_to_iframe(self,reference=None,timeout=10,poll=0.2):
        """iframe 切换
        reference: 可以是frame 的name，id，element对象，索引，locator"""
        if not reference:
            return  self.driver.switch_to.default_content()
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
        el = wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(reference))
        return el

    # 窗口切换
if __name__ == '__main__':
    # 访问百度
    driver = Chrome()
    d = BasePage(driver)
    # 从配置文件当中读取出来
    d.host='http://www.baidu.com'
    # 如果没有优化，每次访问某个页面时，都需要传入完整路径
    d.go_to('/')
    # 输入内容 搜索"紧挨孤独"
    d.fill(('id','kw'),'紧挨孤独')
    d.click(('id','su'))
    time.sleep(3)






