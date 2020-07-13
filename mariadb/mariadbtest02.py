import pymysql

conn = pymysql.connect(host='localhost', 
                        user='root', 
                        password='qwer1234',
                        db='test',
                        charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor
                        ) 
c=conn.cursor()
t=('RHAT',)
sql = "select * from stocks where symbol=%s"
c.execute(sql,t)
print(c.fetchall())
conn.close()