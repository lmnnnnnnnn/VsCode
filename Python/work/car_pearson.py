''' 
@Author: Mengnan Li 
@Date: 2019-10-10 14:27:35 
@Last Modified by: Mengnan Li 
@Last Modified time: 2019-10-10 14:27:35 
'''

import pandas as pd

inputfile = r'C:\svn_home\个人目录\李孟南（）\工作簿1.xlsx'
outputfile = r'C:\Users\sas\Desktop\领动相关系数.xlsx'

data = pd.read_excel(inputfile, index_col=u'PERIOD_START_DT')
data1 = data.corr()[u'SALES']
data1.to_excel(outputfile)