import pymysql
try:
    db=pymysql.connect(host="localhost",
                       user="root",
                       passwd="",
                       port=3306)
    print("Connected")
except:
    print("fail to connect")
cursor=db.cursor()
create_db_path="set_table.sql"
load_data_path="insert_data.sql"
cdb=open(create_db_path,"r", encoding='gb18030').read()
cdb=cdb.split(";")
ldata=open(load_data_path,"r", encoding='utf-8').read()
ldata=ldata.split(";")
for i in cdb:
    if i!='':
        cursor.execute(i+";")
print(cursor.fetchall())
for i in ldata:
    if i!='':
        cursor.execute(i+";")
print(cursor.fetchall())
db.commit()
cursor.execute("SELECT * FROM CUSTOMER")
print(cursor.fetchall())