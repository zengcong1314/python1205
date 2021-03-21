"""python自动化"""
import time
import random

from selenium.webdriver.common.by import By

from web.lesson10_basepage.pages.home import HomePage
from web.lesson10_basepage.pages.login import LoginPage

def gen_class_name():
    """随机生成课程名称，字母，生成10位长度的字母。
    aacdeyualp"""
    name = ''
    for i in range(10):
        letter = random.choice('abcdefghijklmnopqrstuvwxyz')
        name += letter
    return name + str(int(time.time()))

class TestAddClass:
    # 测试类可以不创建吗？可以
    # pytest 当中，测试用例函数可以写在类下面，也可以单独存在

    def test_add_success(self,get_driver):
        """
        运行成功的测试用例
        测试步骤：
        1、打开浏览器
        2、登录老师账号 前置条件
        3、点击创建/加入课程
        4、点击创建课程（课程名称，动态生成，每次都不一样的课程名）
        5、输入课堂名称其他数据
        6、点击创建
        7、出现已经创建好的课程
        8、assert ，如果在首页上出现了课程名称 # 要不要校验数据库 不需要
        # ui 测试 UI界面显示是否正常

        """
        # 获取浏览器
        driver = get_driver
        # 登录老师账号，直接从LoginPage 当中调用 login 方法
        login_page = LoginPage(driver)
        login_page.load().login("wagyu2016@163.com","admin123456")

        # 进入首页
        home_page = HomePage(driver)
        # 先获取所有的课程内容，判断新的课程标题是否已经存在
        # 加一个时间戳
        driver.find_element(By.XPATH,"//span[contains(text(),'创建/加入课程')]").click()
        driver.find_element(By.XPATH,"//a[@id='addClass']").click()
        time.sleep(2)

        # 输入课程名称
        # 随机生成一个课程名称
        class_name = gen_class_name()
        driver.find_element(By.XPATH,"//input[@placeholder='请输入课程名称']").send_keys(class_name)
        time.sleep(2)

        # 点击学期选择下拉框
        driver.find_element(By.XPATH,"//div[@class='yearselbox']").click()
        # 点击自己想要的选项
        driver.find_element(By.XPATH,'//li[text()="2014-2015"]').click()
        # 点击确定
        driver.find_element(By.CSS_SELECTOR,'.pop-btns > .sure').click()
        time.sleep(2)

        # 断言
        # 能不能找到课程 也可以使用 f'//a[text()="{class_name}"]'
        assert driver.find_element(By.XPATH,'//a[text()="{}"]'.format(class_name))

if __name__ == '__main__':
    print(gen_class_name())