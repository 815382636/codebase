import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='weiqi19960906',
    db='person',
    port=3306,
    charset='utf8'
)

cursor = conn.cursor()
cursor.execute('select * from "person";')
rest = cursor.fetchone()
print(rest)