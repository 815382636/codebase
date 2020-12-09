import pymysql
"""
    python 连接mysql 教程
    https://www.runoob.com/python3/python3-mysql.html
"""
db = pymysql.connect('localhost', 'root', 'weiqi19960906', 'mysqltest')
cur = db.cursor()
cur.execute("select * from user;")
data = cur.fetchall()
print(data)
