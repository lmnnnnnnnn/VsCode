''' 
@Author: Mengnan Li 
@Date: 2019-10-16 15:04:57 
@Last Modified by: Mengnan Li 
@Last Modified time: 2019-10-16 15:04:57
查询 
'''

import pandas as pd

inputfile = r'C:\Users\sas\Desktop\FOUND_TIME.xlsx'
outputfile = r'C:\Users\sas\Desktop\相关系数.xlsx'

data = pd.DataFrame(pd.read_excel(inputfile))
outdata = data.query("CARLINE_NM == '名图' & PROVINCE == '河北'")
outdata.to_excel(outputfile)