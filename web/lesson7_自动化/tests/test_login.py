"""
测试登录功能
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login_without_username_and_password(self):
        """测试没有用户名和密码的情况
        尽量通过测试用例的函数名称表示测试的测试点
        if driver.find_element try: drvier.find_element
        梳理测试步骤：
        1、打开浏览器
        2、访问测试页面
        3、点击提交
        4、断言
        """
        driver = webdriver.Chrome()
        url = 'https://v4.ketangpai.com/User/login.html'
        driver.get(url)
        # 定位登录按钮
        login_btn = driver.find_element(By.XPATH,"//div[contains(@class,'pt-login')]/a[@class='btn-btn']")
        login_btn.click()
        # expect 预期结果
        expected = ['账号不能为空','密码不能为空']

        # 实际结果：
        actual = driver.find_elements(By.CLASS_NAME,'error-tips')

        # 两次断言
        # enumerate 可以同时获取索引和值
        """
        for index,el in enumerate(actual):
            # el WebElement
            assert el.text == expected[index]
        
        actual_value = []
        for el in actual:
            actual_value.append(el.text)
        """
        ## 列表推导式
        actual_value = [el.text for el in actual]

        assert expected == actual_value


# 一个用例
# 一个用例变成100个，100个
# 只有用户名
# 只有密码的
# 用户密码错误
# 成功
# 自己的账号
# 老师账号 looker53@sina.com admin123456
# wayu2016@163.com admin123456

# 下节课
# PO模式和优化
