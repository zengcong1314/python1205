import time
from selenium.webdriver.common.by import By




class HomePage():
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
    term_selector_locator = (By.XPATH, "//div[@class='yearselbox']")
    # 点击创建按钮
    create_confirm_locator = (By.CSS_SELECTOR, '.pop-btns > .sure')
    def __init__(self,driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)
        return self
    def get_username(self):
        """获取头像中的登陆用户名"""
        user_elem = self.driver.find_element(*self.avatar_locator) # By.XPATH //*[@class="avatar"]
        return user_elem.get_attribute('title')

    def add_class(self,name,term="2014-2015"):
        """添加课程"""
        driver = self.driver

        driver.find_element(*self.new_class_locator).click()
        driver.find_element(*self.create_class_locator).click()
        time.sleep(2)

        # 输入课程名称
        # 随机生成一个课程名称
        driver.find_element(*self.class_input_locator).send_keys(name)
        time.sleep(2)

        # 点击学期选择下拉框
        driver.find_element(*self.term_selector_locator).click()
        time.sleep(2)
        # 点击自己想要的选项
        driver.find_element(By.XPATH, f'//li[text()="2014-2015"]').click()
        time.sleep(1)
        # 点击确定
        driver.find_element(*self.create_confirm_locator).click()
        time.sleep(2)
        return self

    def get_class(self,name):
        # 根据课程名称定位元素
        el = self.driver.find_element(By.XPATH, '//*[text()="{}"]'.format(name))
        return el