import xlsxwriter 
import os

os.chdir(os.path.dirname(__file__))
  
def create_xl(fname):
    workbook = xlsxwriter.Workbook(fname) 
    worksheet = workbook.add_worksheet()
    return workbook, worksheet

def insert_xl(worksheet, row, column, item):
    worksheet.write(row, column, item) 

def close_xl(workbook):
    workbook.close() 

workbook, worksheet = create_xl('PieChart1.xlsx')
dict_a = {'Independence Day': 10, 'Children\'s Day': 40}

row = 1
insert_xl(worksheet, 0, 0, 'Activity')
insert_xl(worksheet, 0, 1, 'Percentage')

for part in dict_a.items():
    part = list(part)
    insert_xl(worksheet, row, 0, part[0])
    insert_xl(worksheet, row, 1, part[1])
    row += 1

close_xl(workbook)
