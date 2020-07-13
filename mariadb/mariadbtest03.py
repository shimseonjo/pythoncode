import pymysql

conn = pymysql.connect(host='localhost', 
                        user='root', 
                        password='qwer1234',
                        db='test',
                        charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor
                        ) 
c=conn.cursor()

items = [
    ('2020-07-09', 'BUY', 'IBM', 1000, 45.00), 
    ('2020-07-10', 'SELL', 'MSFT', 500, 72.00),
    ('2020-07-11', 'BUY', 'IBM', 800, 53.00), 
    ('2020-07-12', 'SELL', 'RHAT', 100.0, 90.00)
    ]

sql = "insert into stocks values(%s,%s,%s,%s,%s)"
c.executemany(sql, items)
conn.commit()
conn.close()