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
import matplotlib.pyplot as plt
import numpy as np

#参数初始化
inputfile = r'C:\Users\sas\Documents\Python_Study\Python数据分析与挖掘实战\chapter4\demo\data\electricity_data.xls' #供入供出电量数据
outputfile =  r'C:\Users\sas\Desktop\xiansunlv.xls' #属性构造后数据文件

# plt.rcParams['font.sans-serif'] = [u'SimHei'] #用来正常显示中文标签
# plt.rcParams['font.family'] = 'sans-serif'
# plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
# plt.figure(figsize = (7, 5)) #创建图像区域，指定比例

data = pd.read_excel(inputfile) #读入数据
data[u'线损率'] = (data[u'供入电量'] - data[u'供出电量'])/data[u'供入电量']

x = data[u'供入电量']
y = data[u'线损率']
plt.xlabel(u'gongrudianliang')
plt.ylabel(u'xiansunlv')
plt.title(u'供入电量与线损率的关系')
plt.plot(x,y,label = u'供入电量')
plt.legend()
plt.show()

data.to_excel(outputfile, index = False) #保存结果