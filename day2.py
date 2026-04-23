import pymysql
conn=pymysql.connect(host='localhost',
                    user='root', 
                    password='Mahesh@212004')
print("Connection successful")
cursor=conn.cursor()
cursor.execute('use hostel')
cursor.execute('select * from hotel reservations')
tables=cursor.fetchall()
print(tables)
for x in tables:
    print(x)
