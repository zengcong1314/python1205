import time
from selenium.webdriver.common.by import By
from web.lesson10_basepage.common.base import BasePage


class HomePage(BasePage):
    url = 'https://v4.ketangpai.com/Main/index.html'
    # 获取用户头像
    avatar_locator = (By.CSS_SELECTOR,'.avatar')
    # 新建课程/加入课程
    new_class_locator = (By.XPATH, "//span[contains(text(),'创建/加入课程')]")
    # 创建课程
    create_class_locator = (By.XPATH, "//a[@id='addClass']")
    # 课程名称输入框
    class_input_locator = (By.XPATH, "//input[@placeholder='请输入课程名称']")
    # 学期选择框
    term_selector_locator = (By.XPATH, "//div[@class='yearselbox']/p")
    # 点击创建按钮
    create_confirm_locator = (By.CSS_SELECTOR, '.pop-btns > .sure')
    # 加入课程
    add_class_button = (By.XPATH,"//div[contains(text(),'+ 加入课程')]")
    # 课程验证码输入框
    input_class_code = (By.XPATH,"//input[@placeholder='请输入课程加课验证码']")
    # 加入按钮
    add_button = (By.XPATH,"//a[text()='加入']")
    # 更多
    more_button = (By.XPATH,"//span[text()='更多']")
    # 退课
    drop_class = (By.XPATH,"//a[text()='退课']")
    # 登录密码输入框
    input_password_button = (By.XPATH,"//input[@type='password']")
    # 退课
    drop_class_button = (By.XPATH,"//li[@class='dli2']/a")


    def load(self):
        self.driver.get(self.url)
        return self
    def get_username(self):
        """获取头像中的登陆用户名"""
        #TODO：封装获取属性方法
        user_elem = self.driver.find_element(*self.avatar_locator) # By.XPATH //*[@class="avatar"]
        return user_elem.get_attribute('title')

    def add_class(self,name,term="2014-2015"):
        """添加课程"""
        driver = self.driver
        #driver.find_element(*self.new_class_locator).click()
        self.click(self.new_class_locator)
        #driver.find_element(*self.create_class_locator).click()
        self.click(self.create_class_locator)
        time.sleep(2)
        # 输入课程名称
        # 随机生成一个课程名称
        self.fill(self.class_input_locator,name)
        #driver.find_element(*self.class_input_locator).send_keys(name)
        time.sleep(2)
        # 点击学期选择下拉框
        time.sleep(2)
        print("点击下拉框选项元素为：",driver.find_element(*self.term_selector_locator))
        self.click(self.term_selector_locator)
        time.sleep(5)
        #driver.find_element(*self.term_selector_locator).click()
        # 点击自己想要的选项
        #driver.find_element(By.XPATH, '//li[text()="2014-2015"]').click()
        driver.find_element(By.XPATH, f'//li[text()="{term}"]').click()

        # js_code = f"a = document.getElementsByTagName('p')[23];a.innerText ='{term}'"
        # driver.execute_script(js_code)

        # 点击确定
        self.click(self.create_confirm_locator)
        #driver.find_element(*self.create_confirm_locator).click()
        time.sleep(2)
        return self

    def get_class(self,name):
        # 根据课程名称定位元素 f'//*[text()="{name}"]','//*[text()={}]'.format(name)
        el = self.driver.find_element(By.XPATH, f'//*[text()="{name}"]')
        time.sleep(2)
        return el

    def enter_class(self,name):
        locator = (By.XPATH, f'//*[text()="{name}"]')
        self.click(locator)
        return self

    def add_course(self,name):
        self.click(self.add_class_button)
        self.fill(self.input_class_code,name)
        self.click(self.add_button)
        return self

    def delete_course(self,pwd):
        self.click(self.more_button)
        self.click(self.drop_class)
        self.fill(self.input_password_button,pwd)
        self.click(self.drop_class_button)
        return self



