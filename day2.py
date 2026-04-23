import pymysql
conn=pymysql.connect(host='localhost',
                    user='root', 
                    password='Mahesh@212004')
print("Connection successful")
cursor=conn.cursor()
cursor.execute('use hotel')
cursor.execute('select * from hotel_reviews')
tables=cursor.fetchall()
print(tables)
for x in tables:
    print(x)