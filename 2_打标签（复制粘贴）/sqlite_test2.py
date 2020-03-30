import sqlite3

conn=sqlite3.connect('yd.db')

cursor=conn.cursor()
cursor.execute('select * from sampdtl')
values=cursor.fetchall()
print(values)
for value in values:
    print(value)
print(len(values))

cursor.close()
conn.close()