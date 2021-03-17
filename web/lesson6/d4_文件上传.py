import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('file:///D:/zengcong/py37/web/lesson6/d1.html')

# 文件上传
# input 可以直接通过 send_keys 发送文件路径
f = driver.find_element('id','mfile')
time.sleep(3)
f.send_keys(r'D:\zengcong\py37\web\lesson6\总结.md')
time.sleep(2)
