# pip install pypiwin32
# chrom
# 3.7
import win32gui
import win32con

dialog = win32gui.FindWindow("#32770","打开") # 一级窗口
# 找到窗口
ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None) # 二级
comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None) # 三级
edit = win32gui.FindWindowEx(comboBox,0,'Edit',None) # 四级

button = win32gui.FindWindowEx(dialog,0,'Button',None) # 四级

# 操作
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,'D:\\apk.txt') # 发送文件路径
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button) # 点击打开按钮