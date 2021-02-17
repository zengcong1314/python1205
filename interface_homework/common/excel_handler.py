import os
import openpyxl
from interface_homework.config import path
class ExcelHandler:
    def __init__(self,fpath):
        self.fpath = fpath

    def read_dict(self,sheet_name):
        wb = openpyxl.open(self.fpath)
        print(wb)
        ws = wb[sheet_name]
        data = list(ws.values)

        header = data[0]
        all_data = []

        for row in data[1:]:
            row_dict = dict(zip(header,row))
            all_data.append(row_dict)
        return all_data

    def write(self,sheet_name,data,row,column):
        wb = openpyxl.load_workbook(self.fpath)
        ws = wb[sheet_name]
        ws.cell(row=row,column=column).value = data
        wb.save(self.fpath)
        wb.close()

if __name__ == '__main__':
     file = os.path.join(path.data_path,"demo.xlsx")
     xls = ExcelHandler(file)
     excel_data = xls.read_dict('register')
     print(excel_data)


