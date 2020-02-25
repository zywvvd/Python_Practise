'''
xlwt practise py file

2020.2.25
by Yiwei Zhang

https://github.com/zywvvd/Python_Practise
'''

import xlwt

## 建立xlwt对象
xlsx_writer = xlwt.Workbook()


## 建立工作表
test_sheet_1 = xlsx_writer.add_sheet('Test Sheet 1') 
test_sheet_2 = xlsx_writer.add_sheet('Test Sheet 2') 

#try:
    #xlsx_writer.save('write_test.xlsx')   # 保存xlsx
    #xlsx_writer.save('write_test.xls')   # 保存xls
#except Exception as err:
    #print(err)


## 向数据表写入内容
test_sheet_1.write(1,1,123)
test_sheet_1.write(1,2,110)
test_sheet_1.write(1,3,xlwt.Formula("B2+C2"))
test_sheet_1.write(1,4,'test')
test_sheet_1.write(1,5,True)
test_sheet_2.write(3,3,xlwt.Formula("'{}'!$B$2+'{}'!$D$2".format(test_sheet_1.name,test_sheet_1.name)))

#try:
    #xlsx_writer.save('write_test.xlsx')   # 保存xlsx
    #xlsx_writer.save('write_test.xls')   # 保存xls
#except Exception as err:
    #print(err)
    
    
## 设置列宽、行高
test_sheet_1.col(0).width = 400*30 
test_sheet_1.row(0).height = 1000 
#try:
    #xlsx_writer.save('write_test.xlsx')   # 保存xlsx
    #xlsx_writer.save('write_test.xls')   # 保存xls
#except Exception as err:
    #print(err)


## 初始化样式
style = xlwt.XFStyle()  # 样式类实例

## 创建字体
font = xlwt.Font() # 字体类实例
font.name = 'Times New Roman' # 字体名称
font.bold = True # 加粗
font.italic =True # 倾斜
font.height = 300 # 字号 200 为 10 points
font.colour_index=3 # 颜色编码

## 创建边框
borders= xlwt.Borders() # 边框类实例
borders.left= 6
borders.right= 6
borders.top= 6
borders.bottom= 6

## 创建对齐
alignment = xlwt.Alignment() # 对齐类实例
#alignment.horz = xlwt.Alignment.HORZ_LEFT
#alignment.horz = xlwt.Alignment.HORZ_RIGHT
alignment.horz = xlwt.Alignment.HORZ_CENTER      #水平居中 
#alignment.vert = xlwt.Alignment.VERT_TOP
#alignment.vert = xlwt.Alignment.VERT_BOTTOM
alignment.vert = xlwt.Alignment.VERT_CENTER      #垂直居中 
alignment.wrap = 1      # 自动换行

## 创建模式
pattern = xlwt.Pattern() # 模式类实例
pattern.pattern = xlwt.Pattern.SOLID_PATTERN # 固定的样式
pattern.pattern_fore_colour = xlwt.Style.colour_map['yellow'] # 背景颜色

## 应用样式
style.font = font
style.borders = borders
style.num_format_str = '#,##0.0000' # 内容格式
style.alignment = alignment
style.pattern=pattern

## 合并单元格(A,B,C,D) 表示合并左上角[A,C]和右下角[B,D]单元格坐标(均在合并单元格内部)
test_sheet_1.write_merge(3, 5, 3, 5, ' Merge ',style) # ' Merge ' 为写入内容，应用 style 样式

test_sheet_1.write(0, 0, 1234567.890123,style) # 向[0,0]坐标单元格写入数据，应用style样式

try:
    xlsx_writer.save('write_test.xlsx')   # 保存xlsx
    xlsx_writer.save('write_test.xls')   # 保存xls
except Exception as err:
    print(err)
