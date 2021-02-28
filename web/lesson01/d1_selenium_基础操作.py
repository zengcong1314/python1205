# 使用selenium
from selenium import webdriver

# 得到一个浏览器对象
browser = webdriver.Chrome()


# 打开一个网页
page = browser.get("http://www.douban.com")
print(browser.title)
print(browser.current_url)
print(browser.page_source)
# # 刷新页面
# browser.refresh()
# # 访问另外一个网址
# browser.get("http://www.baidu.com")
#
# # back
# browser.back() #退回到豆瓣
#
# # 前进
# browser.forward() # 回到百度
#
# # 最小化
# browser.minimize_window()
# # 最大化
# browser.maximize_window()
# # 全屏
# browser.fullscreen_window()
# # 固定尺寸 px 像素点
# browser.set_window_size(400,300)
# # 关闭标签页
# browser.close()
# 关闭浏览器
browser.quit()
