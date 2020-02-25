'''
xlrd practise py file

2020.2.25
by Yiwei Zhang

https://github.com/zywvvd/Python_Practise
'''

import xlrd


##读取excel文件
try:
    data = xlrd.open_workbook('read_test.xlsx')
except Exception as err:
    print(err)


##获取工作表信息
print(len(data.sheets()))
sheet_names = data.sheet_names()
print(sheet_names)


##通过索引获取工作表内容
info_sheet_1 = data.sheet_by_index(0)
info_sheet_2 = data.sheet_by_index(1)

print(f'sheet :{info_sheet_1.name}  row_num: {info_sheet_1.nrows} column_num: {info_sheet_1.ncols}')
print(f'sheet :{info_sheet_2.name}  row_num: {info_sheet_2.nrows} column_num: {info_sheet_2.ncols}')


##通过名称获取工作表内容
sheet_names = data.sheet_names()
info_sheet_1 = data.sheet_by_name(sheet_names[0])
info_sheet_2 = data.sheet_by_name(sheet_names[1])

print(f'sheet :{info_sheet_1.name}  row_num: {info_sheet_1.nrows} column_num: {info_sheet_1.ncols}')
print(f'sheet :{info_sheet_2.name}  row_num: {info_sheet_2.nrows} column_num: {info_sheet_2.ncols}')


##获取工作表行信息
for i in range(info_sheet_1.nrows):
    print(info_sheet_1.row_values(i))
for i in range(info_sheet_2.nrows):
    print(info_sheet_2.row_values(i))
    
    
##获取工作表列信息
for i in range(info_sheet_1.ncols):
    print(info_sheet_1.col_values(i))
for i in range(info_sheet_2.ncols):
    print(info_sheet_2.col_values(i))
    
    
    
##获取工作表指定位置信息
print(info_sheet_1.cell(2,1).value) 
print(info_sheet_1.cell_value(2,1))
print(info_sheet_1.row(2)[1].value)
print(info_sheet_1.row_values(2)[1])
print(info_sheet_1.col(1)[2].value)
print(info_sheet_1.col_values(1)[2])



##获取工作表中数据的类型
for i in range(info_sheet_1.ncols):
    print(info_sheet_1.cell(2,i).ctype) 
    
    
##获取合并单元格信息
print(info_sheet_1.merged_cells)
    
