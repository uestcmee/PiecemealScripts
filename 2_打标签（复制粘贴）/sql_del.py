import sqlite3

conn=sqlite3.connect('yd.db')

cursor=conn.cursor()
cursor.execute('select * from sampdtl where sampleid=?', ('20181130202900088',))
values=cursor.fetchall()
print(values)
print('\n')

cursor.execute('delete from sampdtl where sampleid= 20181130202900088')
conn.commit()

cursor.execute('select * from sampdtl where sampleid=?', ('20181130202900088',))
values=cursor.fetchall()
print(values)


cursor.close()
conn.close()

