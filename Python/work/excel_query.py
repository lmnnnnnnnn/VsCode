''' 
@Author: Mengnan Li 
@Date: 2019-10-16 15:04:57 
@Last Modified by: Mengnan Li 
@Last Modified time: 2019-10-16 15:04:57
查询 
'''
import pandas as pd

def main():
    inputfile = r'C:\Users\sas\Desktop\FOUND_TIME.xlsx'
    outputfile = r'C:\Users\sas\Desktop\相关系数.xlsx'

    data = pd.DataFrame(pd.read_excel(inputfile))

    # 查
    outdata = data.query("CARLINE_NM == '名图' & PROVINCE == '河北'")

    # 改
    outdata2 = outdata.replace('名图','CF') # 更改表中的名称
    # outdata2 = outdata.rename(columns = lambda x: x.replace('CARLINE_NM','车种'))  # 更改列名
    outdata2.to_excel(outputfile)

if __name__ == "__main__":
    main()