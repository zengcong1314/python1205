import openpyxl

"""打开文件"""
# openpyxl.open()
# open函数没有就用这个,
# 不要在pycharm当中建立excel文件，没有设置excel格式
# 加载demo.xlsx
wb = openpyxl.load_workbook('demo.xlsx')
# 获取表格
ws = wb['register']
# active，默认得表格，一般是打开得第一个表格 效果等于ws = wb['Sheet1']
# ws = wb.active

# 写入数据
ws.cell(row=25,column=2).value = "haha"

# 保存
wb.save('demo.xlsx')

# 退出
wb.close()