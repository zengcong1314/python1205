from selenium.webdriver.common.by import By


class LoginPage:
    my_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/navigation_my"]')
    avatar_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/fragment_my_lemon_avatar_layout"]')
    mobile_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/et_mobile"]')
    pwd_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/et_password"]')
    login_btn_locator = (By.XPATH, '//*[@resource-id="com.lemon.lemonban:id/content"]/android.widget.FrameLayout[1]')

    def __init__(self,driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.my_locator).click()
        self.driver.find_element(*self.avatar_locator).click()
        self.driver.find_element(*self.mobile_locator).send_keys(username)
        self.driver.find_element(*self.pwd_locator).send_keys(password)
        self.driver.find_element(*self.login_btn_locator).click()
        return self
