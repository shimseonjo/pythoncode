import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")
c= conn.cursor()
sql1 ="select * from books where book_id=:id"
c.execute(sql1,id=1)
print(c.fetchall())


conn.close()
