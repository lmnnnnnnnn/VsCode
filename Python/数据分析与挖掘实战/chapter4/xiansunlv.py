# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@Author: mn.l 
@Date: 2019-10-08 21:44:53
@Last Modified by: mn.l 
@Last Modified time: 2019-10-08 21:44:53 
线损率属性构造
'''
import pandas as pd

#参数初始化
inputfile = '/Users/Apology/Documents/Python数据分析与挖掘实战/chapter4/demo/data/electricity_data.xls' #供入供出电量数据
outputfile =  '/Users/Apology/Documents/xiansunlv.xls' #属性构造后数据文件

data = pd.read_excel(inputfile) #读入数据
data[u'线损率'] = (data[u'供入电量'] - data[u'供出电量'])/data[u'供入电量']

data.to_excel(outputfile, index = False) #保存结果