import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")
c= conn.cursor()
sql ="select * from books where title like :1"
title= "%데이%"
c.execute(sql,(title,))
book = c.fetchone()
print(c.fetchall())


conn.close()
