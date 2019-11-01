import pandas as pd
import numpy as np

inputfile = r'C:\Users\sas\Documents\Python_Study\Python数据分析与挖掘实战\chapter3\demo\data\catering_sale.xls'
outputfile = r'C:\Users\sas\Desktop\b.xlsx'

data = pd.read_excel(inputfile)

# print(inputfile.dtypes)
# inputfile['销量'].astype('int')
# a['group'] = np.where(a['销量'] > 4000, 'High', 'Low') 

data.loc[(data['销量'] >= 4000), 'sign'] = 1

data.to_excel(outputfile)
# print(inputfile.shape)