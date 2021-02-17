import random, warnings, xlsxwriter, os

os.chdir(os.path.dirname(__file__))
  
def create_xl(fname):
    workbook = xlsxwriter.Workbook(fname) 
    worksheet = workbook.add_worksheet()
    return workbook, worksheet

def insert_xl(worksheet, row, column, item):
    worksheet.write(row, column, item) 

def close_xl(workbook):
    workbook.close() 

act_str = '''Children's Day
Independence Day
Republic Day
Python Day LOL
'''
act_list = []
percent_list = [0]
add = 0

for act in act_str.split('\n'):
    act_list.append(act)

limit = 100

if (len(act_list) * 10 - limit) > 0:
    limit = int(limit * (len(act_list) * 10 - limit) / 27)
    warnings.warn(f'Percentage limit changed to {limit} because the list of items is very long...')

while True:
    for _ in act_list:
        percent = random.randint(3, 50)
        percent_list.append(percent)

    for j in range(0, len(percent_list)): 
        add = add + percent_list[j]

    if add <= limit:
        break
    else:
        add = 0
        percent_list = [0]

def lstToDict(keys, values):
    len_lst = keys
    res_dct = {keys[i]: values[i] for i in range(0, len(len_lst))}
    return res_dct

percent_list.pop(0)
excel_data_dict = lstToDict(act_list, percent_list)
workbook, worksheet = create_xl('PieChart1.xlsx')
row = 1
insert_xl(worksheet, 0, 0, 'Activity')
insert_xl(worksheet, 0, 1, 'Percentage')

for excel_data in excel_data_dict.items():
    excel_data = list(excel_data)
    insert_xl(worksheet, row, 0, excel_data[0])
    insert_xl(worksheet, row, 1, excel_data[1])
    row += 1

close_xl(workbook)
