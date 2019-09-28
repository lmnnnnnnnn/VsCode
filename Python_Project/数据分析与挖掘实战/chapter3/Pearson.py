# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@Author: mn.l 
@Date: 2019-09-28 21:01:49
@Last Modified by: mn.l 
@Last Modified time: 2019-09-28 21:01:49
餐饮数据相关性分析 
'''
from __future__ import print_function
import pandas as pd

inputfile = r'/Users/Apology/Documents/Python数据分析与挖掘实战/chapter3/demo/data/catering_sale_all.xls'
data = pd.read_excel(inputfile,index_col=u'日期') 

# print(data.corr()) # 相关系数矩阵，即给出了任意两款菜式之间的相关系数
# print(data.corr()[u'百合酱蒸凤爪']) # 只显示‘百合酱蒸凤爪’与其他菜式的相关系数
print('相关系数为：%s' % data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺'])) # 计算'百合酱蒸凤爪'与'翡翠蒸香茜饺'的相关系数