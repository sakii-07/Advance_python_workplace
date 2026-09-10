import psycopg

conn = psycopg.connect(
    user="postgres",
    password="root",
    host = "localhost",
    port=5432,
    dbname="employee"
)

print("connection created successfully")

curser = conn.cursor()

query = "select * from employees"
curser.execute(query)
employees = curser.fetchall()
for emp in employees:
    print(emp)

conn.close()