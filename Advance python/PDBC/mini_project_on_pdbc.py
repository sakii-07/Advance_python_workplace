import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    port = 3306,
    user = 'root',
    password = 'root',
    host = '127.0.0.1'
)

cu = conn.cursor()

def create_db():
    try :
        db_name = input("Enter the database name : ")
        query = f"create database {db_name}"
        cu.execute(query)
        print()
        print("Database created successully ... ")
        print()
        add_history("Database created")
    except Exception as e:
        print(e)

def show_db():
    try:
        query = "show databases"
        cu.execute(query)
        print()
        for database in cu.fetchall():
            print(database[0])
        print()
        add_history("Database showed")
    except Exception as e:
        print(e)

def use_db():
    try :
        db_nm = input("Enter database name to use : ")
        query = f"use {db_nm}"
        cu.execute(query)
        print()
        print("Database selected")
        print()
        add_history("Database used")
    except Exception as e:
        print(e)

def drop_db():
    try:
        db_name = input("Enter database name to delete : ")
        query = f"drop database {db_name}"
        cu.execute(query)
        print()
        print(f"{db_name} database deleted ...")
        print()
        add_history("Database deleted")
    except Exception as e:
        print(e)

def create_table():
    try:
        tb_name = input("Enter table name to create : ")
        n = int(input("Enter number of columns: "))
        columns = []
        for i in range(n):
            col = input(f"Enter column {i+1} name : ")
            data_type = input(f"Enter datatype for {col} : ")
            columns.append(f"{col} {data_type}")
        query  = f"create table {tb_name} ({",".join(columns)})" # id int,
        cu.execute(query)
        print()
        print("Table created successfully ...")
        add_history("table created")
        print()
    except Exception as e:
        print(e)

def show_tables():
    try:
        cu.execute("show tables")
        print()
        for table in cu.fetchall():
            print(table[0])
            add_history("show table")
    except Exception as e:
        print(e)

def desc_table():
    try :
        table_name = input("Enter table name for describe : ")
        desc_table = f"desc {table_name}"
        cu.execute(desc_table)
        print()
        for cols in cu.fetchall():
                print(cols)
        print()
        add_history("Table described")
    except Exception as e:
        print(e)

def drop_table():
    try:
        tb_name = input("Enter table name to delete : ")
        query = f"drop table {tb_name}"
        cu.execute(query)
        print()
        print(f"{tb_name} table deleted successfully ...")
        print()
        add_history("Table droped")
    except Exception as e:
        print(e)    

def rename_table():
    try:
        old_tb_name, new_tb_name = input("Enter the old table name and new table name : ").split()
        query = f"rename table {old_tb_name} to {new_tb_name}"
        cu.execute(query)
        print()
        print("Table re-named successfully ... ")
        print()
        add_history("Table renamed")
    except Exception as e:
        print(e)

def insert_record():
    try:
        tb_name = input("Enter table name to insert values : ")
        n = int(input("Enter number of columns: "))
        columns = []
        values = []
        for i in range(n):
            col = input(f"Enter column {i+1} name : ")
            value = eval(input(f"Enter the value for {col} : "))
            columns.append(f"{col}")
            values.append(f"{value}")
            
        query  = f"insert into {tb_name} ({",".join(columns)}) values ({",".join(['%s']*n)})" # id int,
        cu.execute(query,values)
        conn.commit()
        print()
        print("Data inserted successfully ...")
        print()
        add_history("data inserted")
    except Exception as e:
        print(e)

def view_all_records():
    try:
        tb_name= input("Enter table name : ")
        query = f"select * from {tb_name}"
        cu.execute(query)
        print()
        for rows in cu.fetchall():
            print(rows)
        print()
        add_history("view all records")
    except Exception as e:
        print(e)

def search_records():
    try : 
        table = input("Enter table name  : ")
        id  = eval(input("Enter id : "))
        query = f"select * from {table} where id = {id}"
        cu.execute(query)
        print()
        for data in cu.fetchall():
            print(data)
        add_history("data searched")
    except Exception as e:
        print(e)

def update_records():
    # table = input("Enter table name : ")
    # n = int(input("Enter the number of columns to update"))

    # column = []
    # for i in range(n):
    #     col = input("Enter the column name : ")
    pass

def delete_record():
    try : 
        table = input("Enter table name  : ")
        id  = eval(input("Enter id : "))
        query = f"delete from {table} where id = {id}"
        cu.execute(query)
        conn.commit()
        print()
        print("Record deleted successfully ... ")
        add_history("record deleted")
    except Exception as e:
        print(e)
 
def add_column():
    try:
        table = input("Enter table name : ")
        col = input(f"Enter column name : ")
        dt = input(f"Enter the datatype of {col} : ")
        
        query = f"alter table {table} add ({col} {dt})"
        cu.execute(query)
        print()
        print("Column added successully ... ")
        print()
        add_history("Column added")
    except Exception as e:
        print(e)

def modify_column():
    try:
        table = input("Enter the table name : ")
        col = input("Enter the column name : ")
        dt = input(f"Enter the datatype for {col} : ")
        query = f"alter table {table} modify {col} {dt}"
        cu.execute(query)
        print()
        print("Column modify successfully ... ")
        print()
        add_history("Column modifed")
    except Exception as e:
        print(e)

def drop_column():
    try:
        table = input("Enter the table name : ")
        col = input("Enter the column name : ")
        query = f"alter table {table} drop column {col}"
        cu.execute(query)
        print()
        print("Column deleted successfully ... ")
        print()
        add_history("Column deleted")
    except Exception as e:
        print(e)

def count_records():
    try:
        table = input("Enter table name : ")
        query = f"select count(*) from {table}"
        cu.execute(query)
        print()
        for i in cu.fetchall():
            print(i[0])
        print()
        add_history("Count records")
    except Exception as e:
        print(e)

def max_value():
    try:
        table = input("Enter table name : ")
        column = input("Enter the column : ")
        query = f"select max({column}) from {table}"
        cu.execute(query)
        print()
        for i in cu.fetchall():
            print("Max : ",i[0])
        print()
        add_history("Max value")
    except Exception as e:
        print(e)

def min_value():
    try:
        table = input("Enter table name : ")
        column = input("Enter the column : ")
        query = f"select min({column}) from {table}"
        cu.execute(query)
        print()
        for i in cu.fetchall():
            print("Min : ",i[0])
        print()
        add_history("min value")
    except Exception as e:
        print(e)

def average_value():
    try:
        table = input("Enter table name : ")
        column = input("Enter the column : ")
        query = f"select avg({column}) from {table}"
        cu.execute(query)
        for i in cu.fetchall():
            print("Average : ",i[0])
        print()
        add_history("Average value")
    except Exception as e:
        print(e)

def total():
    try:
        table = input("Enter table name : ")
        column = input("Enter the column : ")
        query = f"select sum({column}) from {table}"
        cu.execute(query)
        print()
        for i in cu.fetchall():
            print("Sum : ",i[0])
        print()
        add_history("toatl")
    except Exception as e:
        print(e)

def sort_asc():
    try:
        table = input("Enter table name : ")
        column = input("Enter column name to sort in ascending : ")
        query = f"select * from {table} order by {column}"
        cu.execute(query)
        print()
        for data in cu.fetchall():
            print(data)
        print()
        add_history("Data Sorted in ascending order")
    except Exception as e:
        print(e)

def sort_desc():
    try:
        table = input("Enter table name : ")
        column = input("Enter column name to sort in descending : ")
        query = f"select * from {table} order by {column} desc"
        cu.execute(query)
        print()
        for data in cu.fetchall():
            print(data)
        print()
        add_history("Data Sorted in descending order")
    except Exception as e:
        print(e)

def command():
     print("""
    ========== DATABASE OPERATIONS =========

        1. Create Database
        2. Show Databases
        3. Use Database
        4. Drop Database

        5. Create Table
        6. Show Tables
        7. Describe Table
        8. Drop Table
        9. Rename Table

        10. Insert Record
        11. View Records
        12. Search Record
        13. Update Record
        14. Delete Record

        15. Add Column
        16. Modify Column
        17. Drop Column

        18. Count Records
        19. Max Value
        20. Min Value
        21. Average Value
        22. Sum

        23. Sort Ascending
        24. Sort Descending

        25. Exit
        """)


while True:
    command()
    ch = int(input("Enter Choice : "))

    if ch == 1:
        create_db()
    elif ch == 2:
        show_db()
    elif ch == 3:
        use_db()
    elif ch == 4:
        drop_db()
    elif ch == 5:
        create_table()
    elif ch == 6:
        show_tables()
    elif ch == 7:
        desc_table()
    elif ch == 8:
        drop_table()
    elif ch == 9:
        rename_table()
    elif ch == 10:
        insert_record()
    elif ch == 11:
        view_all_records()
    elif ch == 12:
        search_records()
    elif ch == 13:
        update_records()
    elif ch == 14:
        delete_record()
    elif ch == 15:
        add_column()
    elif ch == 16:
        modify_column()
    elif ch == 17:
        drop_column()
    elif ch == 18:
        count_records()
    elif ch == 19:
        max_value()
    elif ch == 20:
        min_value()
    elif ch == 21:
        average_value()
    elif ch == 22:
        total()
    elif ch == 23:
        sort_asc()
    elif ch == 24:
        sort_desc()
    elif ch == 25:
        break
    else:
        print("Invalid choice")

history = []

def add_history(action):
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    history.append(f"{current_time} - {action}")