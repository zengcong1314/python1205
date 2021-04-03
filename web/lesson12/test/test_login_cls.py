"""
测试登录功能
"""
import time
import allure
import pytest
from web.lesson11_pre.common.logger_hander import logger
from web.lesson11_pre.pages.login import LoginPage
from web.lesson11_pre.pages.home_ba import HomePage
from web.lesson11_pre.data import login

@allure.feature("登录功能")
class TestLogin:
    @allure.title("测试用户名和密码为空")
    def test_login_without_username_and_password(self,get_driver):
        # 在测试用例函数中接收fixture 中的返回值，不需要加括号
        # 初始化页面对象
        driver = get_driver
        login_page = LoginPage(driver)

        # 获取实际结果
        actual_value = login_page.load().login('','').get_error_msgs()
        #login_page.load(url)
        """
        # 登录
        login_page.login(driver,'','')
        # 获取错误信息
        actual_value = login_page.get_error_msgs()
        """
        # 断言
        expected = ['账号不能为空', '密码不能为空']
        # driver.get_screenshot_as_file('demo.png')
        login_page.screenshot()
        # 测试报告当中生成截图,get_screenshot_as_png()不需要传文件名称与路径，保存的是二进制数据，把数据保存在测试报告中
        allure.attach(driver.get_screenshot_as_png(),
                      name='测试结果截图',
                      attachment_type='png')
        try:
            assert expected == actual_value
        except AssertionError as e:
            logger.error(f"断言失败{e}")
            # 不抛出异常，所有的用例都是通过的
            # 现在页面的截图，保存到本地
            driver.get_screenshot_as_file('demo.png')
            raise e

    @allure.title("测试用户名为空")
    #@pytest.mark.parametrize('info',[('','ab','账号不能为空')])
    def test_login_without_username(self,get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        actual_value = login_page.load().login('', 'as').get_error_msgs()
        expected = '账号不能为空'
        assert actual_value[0] == expected

    @allure.title("登陆成功")
    @pytest.mark.parametrize('info',login.success)
    def test_login_student_success(self,get_driver,info):
        username,password,expected = info
        driver = get_driver
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        # 访问url
        login_page.load()
        login_page.login(username, password)

        # 断言页面标题
        time.sleep(0.5)
        assert driver.current_url == home_page.url
        # 首页行为
        actual = home_page.get_username()
        assert actual == expected

    # def test_login_teacher_success(self,get_driver):
    #     driver = get_driver
    #     login_page = LoginPage(driver)
    #     home_page = HomePage(driver)
    #     # 访问url
    #     login_page.load()
    #     login_page.login('wagyu1016@163.com', 'admin123456')
    #
    #     # 断言页面标题
    #     time.sleep(0.5)
    #     assert driver.current_url == home_page.url
    #     # 首页行为
    #     actual = home_page.get_username()
    #     assert actual == 'wagyu'
