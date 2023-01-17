import mysql.connector

#连接数据库
mydb = mysql.connector.connect(
   host='',
   user='root',
   password='',
)
mycursor=mydb.cursor()

 #新建数据表
mycursor.execute('CREATE DATABASE CFPS2010')
mycursor.execute('CREATE DATABASE CFPS2012')
mycursor.execute('CREATE DATABASE CFPS2014')
mycursor.execute('CREATE DATABASE CFPS2016')
mycursor.execute('CREATE DATABASE CFPS2018')

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
