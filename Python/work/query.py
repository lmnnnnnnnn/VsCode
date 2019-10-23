import pandas as pd

inputfile = r'C:\svn_home\个人目录\李孟南（）\2222.xlsx'
outputfile = r'C:\Users\sas\Desktop\查询结果.xlsx'
data = pd.DataFrame(pd.read_excel(inputfile))
    
def main():
    print(data.columns.values)
    row = input("请输出行名称:")
    information = input("请输入查询内容:")

    if row in data:
        result = data.loc[data[row] == information]
        print("查询成功")
        result.to_excel(outputfile)
    else:
        print("输入信息有误")