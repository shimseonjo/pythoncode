import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")
c= conn.cursor()

item =('데이터분석실무','2020-07-13','위키북스',300,10)   
sql= '''insert into books
                    values(book_seq.NEXTVAL,:1,:2,:3,:4,:5)'''
 
c.execute(sql,item)
conn.commit()
conn.close()
