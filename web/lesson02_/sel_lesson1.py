from selenium import webdriver

#
driver = webdriver.Chrome(service_log_path="D:\\chromdriver_server.log")

#
driver.get("http://www.baidu.com")
