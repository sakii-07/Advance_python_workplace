import mysql.connector

conn = mysql.connector.connect(
    user = "root",
    port= 3306,
    host = "127.0.0.1",
    password = "root",
    database = 'jbk_1319' 
)

cu = conn.cursor()
def create_db():
    try:
        db_name = input("Enter database name to create : ")
        create_db = f"create database {db_name}"
        cu.execute(create_db)
    except Exception as e:
        print(e)

try :
    db_nm = input("Enter database name to use : ")
    use_db = f"use {db_nm}"
    cu.execute(use_db)

except Exception as e:
    print(e)

try:
    show_table = "show tables"
    cu.execute(show_table)
except Exception as e:
    print(e)
else:
    for table_name in cu.fetchall():
        print(table_name)

try :
    table_name = input("Enter table name for describe : ")
    desc_table = f"desc {table_name}"
    cu.execute(desc_table)
except Exception as e:
    print(e)
else:
    for cols in cu.fetchall():
        print(cols)

def insert_data():
    try : 
        tb_name, col1, col2, col3,col4 = input("Enter table name, and colums 1,2,3,4: ").split()
        id,name,age,city = input("Enter the id, name, age, city : ").split()
        # print(tb_name,col1,col2,col3)
        insert_data = "insert into {0} ({1},{2},{3},{4}) values(%s,%s,%s,%s)".format(tb_name,col1,col2,col3,col4)
        data = (int(id),name,int(age),city)
    except Exception as e:
        print(e)
    else:
        cu.execute(insert_data,data)
        conn.commit()

        print(f"*************** {tb_name} *********************")
        cu.execute(f"select * from {tb_name}")
        for data in cu.fetchall():
            print(data)

def delete_data():
    try : 
        table, del_value = input("Enter table name and id to delete : ").split()
        delete_data = f"delete from {table} where id = {int(del_value)}"
        cu.execute(delete_data)
        conn.commit()
    except Exception as e:
        print(e)
    else:
        print(f"*************** {table} *********************")
        cu.execute(f"select * from {table}")
        for data in cu.fetchall():
            print(data)

def drop_table():
    table = input("Enter table name to drop : ")
    drop_table = f"drop table {table}"
    cu.execute(drop_table)
    conn.commit()

    cu.execute("show tables")
    for tables in cu.fetchall():
        print(tables)

cu.close()
conn.close()
