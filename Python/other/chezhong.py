# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@Author: mn.l 
@Date: 2019-09-29 21:03:44
@Last Modified by: mn.l 
@Last Modified time: 2019-09-29 21:03:44 
'''
from __future__ import print_function
import pandas as pd

def mining():
    inputfile = r'C:\svn_home\系统测试\竞争力分析结果\车种竞争力_李岳思路.xlsx'
    data = pd.read_excel(inputfile,index_col=u'时间(Time)',sheet_name=2)

    data = data[(data[u'本品最低市场价平均值(Avg_1)'] > 400) & (data[u'本品最低市场价平均值(Avg_1)'] < 100000)]
    # print(data.corr()) # 相关系数矩阵，即给出了任意两列之间的相关系数
    outfile = data.describe()
     # print(data.sum())
    # print(data.corr()[u'']) # 只显示‘百合酱蒸凤爪’与其他菜式的相关系数
    # print('相关系数为：%s' % data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺'])) # 计算'百合酱蒸凤爪'与'翡翠蒸香茜饺'的相关系数
    outfile.to_excel(r'C:\Users\sas\Desktop\aaa.xlsx',)


mining()
if __name__ == "__mining__":
    mining