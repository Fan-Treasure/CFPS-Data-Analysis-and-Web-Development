import mysql.connector

# 连接数据库
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='202000830046xjl',
)
mycursor = mydb.cursor()

# 新建数据表
mycursor.execute('CREATE DATABASE CPFS2010')
mycursor.execute('CREATE DATABASE CPFS2012')
mycursor.execute('CREATE DATABASE CPFS2014')
mycursor.execute('CREATE DATABASE CPFS2016')
mycursor.execute('CREATE DATABASE CPFS2018')

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
