# 拉格朗日插值代码
import pandas as pd #导入数据分析库，Pandas
from scipy.interpolate import lagrange #导入拉格朗日插值函数

inputfile = r'C:\Users\sas\Documents\Python_Study\Python数据分析与挖掘实战\chapter4\demo\data\catering_sale.xls'
outputfile = r'C:\Users\sas\Desktop\拉格朗日法.xlsx'

data = pd.read_excel(inputfile)  #读入数据
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000) ] = None #过滤异常值，将其变为空值

#自定义列向量插值函数
#s为列向量, n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] #取数
    y = y[y.notnull()] #剔除空值
    return lagrange(y.index, list(y))(n)  #插值并返回差值结果

#逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]: #如果为空即插值
            data[i][j] = ployinterp_column(data[i], j)

data.to_excel(outputfile)