import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")
c= conn.cursor()

items=[
        ('빅데이터','2020-07-15','이지퍼블리싱',599,67),
        ('안드로이드','2020-07-17','삼성',120,8),
        ('spring','2020-07-19','위키북스',489,39)
    ]
sql= '''insert into books
                    values(book_seq.NEXTVAL,:1,:2,:3,:4,:5)'''
 
c.executemany(sql,items)
conn.commit()
conn.close()
