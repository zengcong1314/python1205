"""文件上传
1、send_keys：一定要是input 元素
2、现在文件上传的元素不是input，而是div
只能借助第三方工具，上传文件时，打开的窗口
window:
pywinauto
pyautogui 跨平台
"""
from pywinauto.keyboard import send_keys
import pywinauto
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('file:///D:/zengcong/py37/web/lesson7_文件上传/上课代码/d1.html')

# 文件上传
# input 可以直接通过 send_keys 发送文件路径
f = driver.find_element('id','mfile')
time.sleep(3)
#触发点击事件，让系统的弹框出来
f.click()

# 等待,因为弹框弹出来需要时间 不能用显性等待，不在selenium里面
time.sleep(3)
# pywinauto 的send_keys
send_keys(r'D:\zengcong\py37\web\lesson7_文件上传\性能测试总结2.png')
# 确认提交,确定
send_keys('{VK_RETURN}')
time.sleep(3)