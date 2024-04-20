import pymysql
import pandas as pd
from sqlalchemy import create_engine
 
# 读取你要存储的数据
data = pd.read_csv('D:/3170/data/Manufacturers.csv', sep=',', low_memory=False)
print(data.shape)
# mysql+pymysql://用户名:密码@IP地址/数据库名?charset=UTF8MB4
engine = create_engine('mysql+pymysql://root:Hyx20030716.@127.0.0.1:3306/tire_company?charset=utf8')
data.to_sql('Manufacturer',engine,index=False,if_exists='replace')
'''
'china2018'是你要保存表的名字；
index=False:表示需不需要将csv数据的index进行存储
if_exists： 三个模式：fail，若表存在，则不输出；replace：若表存在，覆盖原来表里的数据；append：若表存在，将数据写到原表的后面。默认为fail
'''
print('导入成功')