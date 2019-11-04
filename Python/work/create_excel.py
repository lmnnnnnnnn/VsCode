import pandas as pd
def create_excel():
    excel = pd.DataFrame({'ID':[1,2,3],'name':['xiaohong','xiaolan','xiaohua']})
    ex = excel.set_index('ID')
    ex.to_excel(r'C:\Users\sas\Desktop\创建.xls')

create_excel()