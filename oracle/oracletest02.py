import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")
c= conn.cursor()
sql='CREATE SEQUENCE book_seq START WITH 1 INCREMENT BY 1'
c.execute(sql)
sql='''create table  books(
                        book_id  number not null,
                        title VARCHAR2(50),
                        published_date VARCHAR2(50),
                        publisher VARCHAR2(50),
                        pages number,
                        recommend number,
                        CONSTRAINT pk_book PRIMARY KEY(book_id))'''
c.execute(sql)
conn.close()
