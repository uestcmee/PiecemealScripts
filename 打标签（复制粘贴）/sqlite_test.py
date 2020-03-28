import sqlite3

conn=sqlite3.connect('yd.db')

cursor=conn.cursor()
cursor.execute('select * from sample where id=?', ('20181129172910708',))
values=cursor.fetchall()
print(values)
print('\n')

cursor.execute('delete from sample where id= 20181130202900088')
conn.commit()

cursor.execute('select * from sample where id=?', ('20181129172910708',))
values=cursor.fetchall()
print(values)


cursor.close()
conn.close()


