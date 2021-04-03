import time
from selenium.webdriver.common.by import By
from web.lesson11_pre.common.base import BasePage


class ClassPage(BasePage):
    # enter_class
    attance_locator = (By.CSS_SELECTOR,'.K_left_middle_attance > a')
    # 跳过弹框
    skip_welcome_locator = (By.XPATH,'//*[text()="跳过"]')
    # 新建考勤
    new_attance_locator = (By.CSS_SELECTOR,'.attend_headright > a')
    # data_attance
    data_attance_locator = (By.XPATH,'//span[text()="数字考勤"]')
    # 开始考勤
    start_attance_locator = (By.XPATH,'//div[@id="new-perform"]//a[text()="开始考勤"]')
    # attend_code
    attend_code_locator = (By.CSS_SELECTOR,'.number-box >span')
    # 签到
    sign_class_locator = (By.XPATH,'//a[text()="立即签到"]')
    # 输入签到码
    sign_locator = (By.ID,'phoneVer_modalAuthInput')
    # 获取加课码
    class_code = (By.XPATH,"//div[@class='codetext']")
    # 出勤状态
    status = (By.XPATH,"//span[text()='出勤']")
    # 结束签到
    end_sign_button = (By.XPATH,"//div[@id='number-attend']//a[text()='结束']")
    # 确认结束
    confirm_end_sign = (By.XPATH,"//div[@id='end-attend']//a[text()='结束']")
    # //div[text()='考勤详情']
    detail_sign = (By.XPATH,"//div[text()='考勤详情']")

    def skip_welcome(self):
        self.click(self.skip_welcome_locator)
        return self

    def get_class_code(self):
        """获取签到码"""
        self.click(self.attance_locator)
        time.sleep(2)
        self.switch_to_iframe('layui-layer-content1')
        #self.driver.switch_to.frame('layui-layer-content1')
        # 新建考勤
        time.sleep(2)
        self.click(self.new_attance_locator)
        # 点击数字考勤
        time.sleep(2)
        self.click(self.data_attance_locator)
        # 开始考勤
        time.sleep(2)
        self.click(self.start_attance_locator)
        # find_elements
        numbers = self.find_elements(self.attend_code_locator)
        time.sleep(2)
        #numbers = self.driver.find_elements(*self.attend_code_locator)
        # 也可以用拼接字符串
        """
        number = ''
        for num in numbers:
            number += num.text
        return number
        """
        # 列表推导式，
        return [number.text for number in numbers]

    def sign(self,code):
        """学生签名"""
        self.click(self.sign_class_locator)
        time.sleep(1)
        self.fill(self.sign_locator,code)
        return self

    def get_addclass_code(self):
        code = self.find_element(self.class_code).text
        return code

    def get_status(self):
        status = self.find_element(self.status)
        # print(*self.status)
        # print(self.status)
        return status.text

    def end_sign(self):
        self.click(self.end_sign_button)
        time.sleep(1)
        self.click(self.confirm_end_sign)
        time.sleep(2)
        self.click(self.detail_sign)
        return self








