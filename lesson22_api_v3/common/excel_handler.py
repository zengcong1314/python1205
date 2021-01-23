"""excel操作"""
from pprint import pprint

import openpyxl
class ExcelHandler:
    def __init__(self,fpath):
        self.fpath = fpath
    # 读取为元组
    def read_tuple(self,sheet_name):
        """读取数据"""
        # 打开文件
        wb = openpyxl.open(self.fpath)
        print(wb)
        # 获取表格
        ws = wb[sheet_name]
        data = list(ws.values)
        return data[1:]
    # 读取为字典
    def read_dict(self,sheet_name):
        """读取数据"""
        # 打开文件
        wb = openpyxl.open(self.fpath)
        #print(wb)
        # 获取表格
        ws = wb[sheet_name]
        data = list(ws.values)
        #print(data)
        header = data[0]
        #print(header)
        #print(data[1:])
        all_data = []
        for row in data[1:]:
            row_dict = dict(zip(header,row))
            #print(row_dict)
            all_data.append(row_dict)
        return all_data

# 直接敲main
if __name__ == '__main__':
    xls = ExcelHandler('test_data.xlsx')
    excel_data1 = xls.read_tuple('test')
    excel_data2 = xls.read_dict('test')
    print(excel_data1)
    print(excel_data2)
