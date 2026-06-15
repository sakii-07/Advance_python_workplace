'''
PDBC = Python database connectivity
library -- 1) mysql connector
           2) pymysql

pip install mysql-coonector-python
pip list
'''
import mysql.connector

conn = mysql.connector.connect(
    user = "root",
    port= 3306,
    host = "127.0.0.1",
    password = "root",
    database = 'jbk_1319' 
)

# print("Conn success")

# import pymysql

# conn = pymysql.connect(
#     user = 'root',
#     password = 'root',
#     host = '127.0.0.1',
#     database = 'jbk_1319',
#     port = 3306
# )

cu = conn.cursor()
print("curser con successfully")

create_database = "Create database pdbc_1319"

try :
    cu.execute(create_database)
    print("Database created successfully ")
except Exception as e:
    print(e)

cu.execute("use pdbc_1319")

createTable = "create table if not exists stud_info (sid int primary key, sname varchar(32), age int)"
cu.execute(createTable)

print("Table created successfully")

insert_data = "insert into stud_info (sid,sname,age) values (%s, %s, %s)"
data = ((1,'sakshi',23),(2,'Divya',34))

try:
    cu.executemany(insert_data,data)
    print("data inserted successfully")
except Exception as e:
    print(e)

# # fetch data
# show = "select * from stud_info"
# cu.execute(show)

# data = cu.fetchone()
# print(data)

# for i in cu.fetchall():
#     print(i)

selectbyId = "select * from stud_info where sid = %s"
id = (1,)

cu.execute(selectbyId,id)
d = cu.fetchone()
print(d)
cu.close()
conn.close()