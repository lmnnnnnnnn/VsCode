# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@Author: mn.l 
@Date: 2019-10-02 15:45:14
@Last Modified by: mn.l 
@Last Modified time: 2019-10-02 15:45:14 
'''
import pandas as pd
import numpy as np

datafile = '/Users/Apology/Documents/Python数据分析与挖掘实战/chapter4/demo/data/normalization_data.xls'
data = pd.read_excel(datafile, header = None) #读取数据

print((data - data.min())/(data.max() - data.min())) #最小-最大规范化
print((data - data.mean())/data.std()) #零-均值规范化
print(data/10**np.ceil(np.log10(data.abs().max()))) #小数定标规范化