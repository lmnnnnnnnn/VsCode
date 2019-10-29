import pandas as pd
import numpy as np


# 创建数据表信息
df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
                   "date":pd.date_range('20130102', periods=6),
                   "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age":[23,44,54,32,34,32],
                   "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
                   "price":[1200,np.nan,2133,5433,np.nan,4432]},
                   columns =['id','date','city','category','age','price'])

# 查看数据表的纬度
df.shape
# 查看数据表的纬度
df.info()
# 查看数据表各列格式
print(df.dtypes)
# 查看单列格式
print(df['id'].dtype)
# 检查是否空值
print(df.isnull())
# 检查特定列空值
print(df['price'].isnull())
# Unique是查看唯一值的函数,只能对特定列进行检查
# 查看city列中的唯一值
print(df['city'].unique())
# 查看数据表数值
print(df.values)
# 查看列名称
print(df.columns)
# 查看前10行的数据
print(df.head())
# 查看前三行的数据
print(df.head(n=3))
# 查看后三行的数据
print(df.tail(n=1))
# 删除数据表中含有空值的行
print(df.dropna(how='any'))
# 使用数字0填充数据表中的空值
df.fillna(value=0)
# 使用price均值对na进行填充
df['price'].fillna(df['price'].mean())
# 清理city字段中的字符空格
df['city']=df['city'].map(str.strip)
# city列大小写转换
df['city']=df['city'].str.lower()
# 更改数据格式
df['price'].astype('int')
# 更改列名称
df.rename(columns={'category':'category-size'})
# 删除重复值
df['city']
df['city'].drop_duplicates()
# 数据替换
df['city'].replace('sh','shanghai')