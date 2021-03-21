class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def click(self,locator:tuple,force=False):
        """点击"""
        el = self.driver.find_element(*locator)
        # 有时候，当元素不可点击的时候，使用el.click 不生效
        if not force:
            self.driver.execute_script("arguments[0].click()",el)
        else:
            self.driver.execute_script("arguments[0].click({force:ture})", el)
        return self

    def fill(self,locator,text):
        """输入内容"""
        el = self.driver.find_element(*locator)
        el.send_keys(text)
        return self


