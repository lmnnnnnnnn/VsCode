''' 
@Author: Mengnan Li 
@Date: 2019-09-22 21:50:43 
@Last Modified by: Mengnan Li 
@Last Modified time: 2019-09-22 21:50:43 
'''
# coding=utf-8
import xlrd
# data = xlrd.open_workbook('C:/svn_home/个人目录/李孟南（）/其他/车种排量.xls')
# table = data.sheets()[0]
# nrows = table.nrows
# for i in range(nrows):
#     if i == 0:
#         continue
#     print(table.row_values(i)[12])


# import xlwt
#
#
# def readfile():
#     # 设置路径
#     path = 'C:/svn_home/个人目录/李孟南（）/其他/车种排量.xls'
#     # 打开excel
#     data = xlrd.open_workbook(path)
#     # 读取共有多少个工作表，表名为
#     sheet_num = data.nsheets
#     names = data.sheet_names()
#     print("共有{}个工作表，表名为{}".format(sheet_num, names))
#     sheet = data.sheet_by_name("Sheet 1")
#     # 读取行数和列数
#     rows = sheet.nrows
#     cols = sheet.nrows
#     print("Sheet 1：{}行×{}列".format(rows, cols))
#
#     for i in range(rows):
#         for j in range(cols):
#             content = sheet.cell(i,j).value
#             book = xlwt.Workbook(encoding='utf-8')  # 创建一个Excel对象
#     sheet1 = book.add_sheet('sheet1')  # 添加一个名为sheet1的sheet
#     sheet1.write(i, j, content)  # 在索引为i, j处写入content
#     book.save("C:/Users/sas/Desktop/output.xls")  # 保存
#
# readfile()

def openfile():
    data = xlrd.open_workbook(
        r"C:\Users\sas\Desktop\Mengnan Li-工作日志-2019.xlsx")
    # 读取共有多少个工作表，表名为
    sheet_num = data.nsheets
    names = data.sheet_names()
    print("共有{}个工作表，表名为{}".format(sheet_num, names))
    # 可以通过函数、索引、名称获得工作表
    sheet_1_by_function = data.sheets()[0]
    sheet_1_by_index = data.sheet_by_index(0)
    sheet_1_by_name = data.sheet_by_name('Timesheet')
    # 可以通过方法获得某一列或者某一行的数值
    sheet_1_by_name.row_values(1)
    sheet_1_by_name.col_values(1)
    # 通过工作表的属性获得行数和列数
    n_of_rows = sheet_1_by_name.nrows
    n_of_cols = sheet_1_by_name.ncols
    sheets = data.sheets()
    # 循环来遍历一次文件
    for i in range(n_of_rows):
        print(sheet_1_by_name.row_values(i))


openfile()
