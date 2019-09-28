#-*- coding:utf-8 -*-
#汽车数据分析
from __future__ import print_function
import pandas as pd

inputfile = r'C:\Users\sas\Desktop\YC.xlsx'

# outputfile = r'C:\Users\sas\Desktop\a.xlsx'
data = pd.read_excel(inputfile,index_col = u'本品车种名(First_Car_Name)',sheet_name=1)
data = data[(data[u'本品最低市场价平均值(Avg_1)'] > 400) & (data[u'本品最低市场价平均值(Avg_1)'] < 65000)]
statistics = data.describe() 
print(statistics)

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min']
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean']
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%']

print(statistics)