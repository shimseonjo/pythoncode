import sqlite3,csv

input_file = 'sqlite/input.csv'

conn = sqlite3.connect('sqlite/suppliers.db')

c= conn.cursor()

sql = '''
        create table if not exists suppliers(
            supplier_name varchar(20),
            invoice_number varchar(20),
            part_number varchar(20),
            cost float,
            purchase_date date
        )'''

c.execute(sql)
sql = "delete from suppliers"
c.execute(sql)
conn.commit()

file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header = next(file_reader,None)
next()

data=[]
for row in file_reader:
    data.append(row)    

sql = 'insert into suppliers values(?,?,?,?,?)'
c.executemany(sql,data)
conn.commit()
c.close()
conn.close()