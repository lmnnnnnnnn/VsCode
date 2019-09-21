import pandas as pd
from numpy import nan as NA

xlsx = pd.ExcelFile(r"C:\Users\sas\Documents\SAS（北京现代）相关\111.xlsx")
a = pd.read_excel(xlsx, 'Sheet1')
print(a.describe())