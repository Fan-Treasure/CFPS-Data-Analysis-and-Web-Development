from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.dialects.mysql import LONGTEXT
import mysql.connector
import csv
from tqdm import tqdm

# 读取csv中的数据按行展示
with open("E:/CPFS/CPFS2018/DATA/2018childproxy.csv", "rt", encoding="utf-8") as vsvfile:
    reader = csv.reader(vsvfile)
    rows = [row for row in reader]
label_name = rows[0][0]
value_name = '%s'
row_name = rows[0][0]
for i in range(len(rows[0]) - 1):
    row_name = row_name + ' LONGTEXT, ' + rows[0][i + 1]
    label_name = label_name + ' , ' + rows[0][i + 1]
    value_name = value_name + ' , %s'

whole_name = 'CREATE TABLE CPFS2018_childproxy (' + row_name + ' LONGTEXT) Engine=MyISAM DEFAULT CHARSET=utf8'

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='CPFS2018'
)
mycursor = mydb.cursor()

# sql = "DROP TABLE CPFS2018_childproxy"
#
# mycursor.execute(sql)

# 新建数据表
mycursor.execute(whole_name)

# 插入数据
sql = 'INSERT INTO CPFS2018_childproxy (' + label_name + ') VALUES (' + value_name + ')'
for i in tqdm(range(len(rows))):
    val = tuple(rows[i])
    mycursor.execute(sql, val)
    mydb.commit()
print('mission1 complete')

# 读取csv中的数据按行展示
with open("E:/CPFS/CPFS2018/DATA/2018crossyearid.csv", "rt", encoding="utf-8") as vsvfile:
    reader = csv.reader(vsvfile)
    rows = [row for row in reader]
label_name = rows[0][0]
value_name = '%s'
row_name = rows[0][0]
for i in range(len(rows[0]) - 1):
    row_name = row_name + ' LONGTEXT, ' + rows[0][i + 1]
    label_name = label_name + ' , ' + rows[0][i + 1]
    value_name = value_name + ' , %s'

whole_name = 'CREATE TABLE CPFS2018_crossyearid (' + row_name + ' LONGTEXT) Engine=MyISAM DEFAULT CHARSET=utf8'

# 连接数据库
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='202000830046xjl',
    database='CPFS2018'
)
mycursor = mydb.cursor()

# sql = "DROP TABLE CPFS2018_crossyearid"
#
# mycursor.execute(sql)

# 新建数据表
mycursor.execute(whole_name)

# 插入数据
sql = 'INSERT INTO CPFS2018_crossyearid (' + label_name + ') VALUES (' + value_name + ')'
for i in tqdm(range(len(rows))):
    val = tuple(rows[i])
    mycursor.execute(sql, val)
    mydb.commit()
print('mission2 complete')

# 读取csv中的数据按行展示
with open("E:/CPFS/CPFS2018/DATA/2018famconf.csv", "rt", encoding="utf-8") as vsvfile:
    reader = csv.reader(vsvfile)
    rows = [row for row in reader]
label_name = rows[0][0]
value_name = '%s'
row_name = rows[0][0]
for i in range(len(rows[0]) - 1):
    row_name = row_name + ' LONGTEXT, ' + rows[0][i + 1]
    label_name = label_name + ' , ' + rows[0][i + 1]
    value_name = value_name + ' , %s'

whole_name = 'CREATE TABLE CPFS2018_famconf(' + row_name + ' LONGTEXT) Engine=MyISAM DEFAULT CHARSET=utf8'

# 连接数据库
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='202000830046xjl',
    database='CPFS2018'
)
mycursor = mydb.cursor()

# sql = "DROP TABLE CPFS2018_famconf"
#
# mycursor.execute(sql)

# 新建数据表
mycursor.execute(whole_name)

# 插入数据
sql = 'INSERT INTO CPFS2018_famconf (' + label_name + ') VALUES (' + value_name + ')'
for i in tqdm(range(len(rows))):
    val = tuple(rows[i])
    mycursor.execute(sql, val)
    mydb.commit()
print('mission3 complete')

# 读取csv中的数据按行展示
with open("E:/CPFS/CPFS2018/DATA/2018famecon.csv", "rt", encoding="utf-8") as vsvfile:
    reader = csv.reader(vsvfile)
    rows = [row for row in reader]
label_name = rows[0][0]
value_name = '%s'
row_name = rows[0][0]
for i in range(len(rows[0]) - 1):
    row_name = row_name + ' LONGTEXT, ' + rows[0][i + 1]
    label_name = label_name + ' , ' + rows[0][i + 1]
    value_name = value_name + ' , %s'

whole_name = 'CREATE TABLE CPFS2018_famecon(' + row_name + ' LONGTEXT) Engine=MyISAM DEFAULT CHARSET=utf8'

# 连接数据库
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='202000830046xjl',
    database='CPFS2018'
)
mycursor = mydb.cursor()

# sql = "DROP TABLE CPFS2018_famecon"
#
# mycursor.execute(sql)

# 新建数据表
mycursor.execute(whole_name)

# 插入数据
sql = 'INSERT INTO CPFS2018_famecon (' + label_name + ') VALUES (' + value_name + ')'
for i in tqdm(range(len(rows))):
    val = tuple(rows[i])
    mycursor.execute(sql, val)
    mydb.commit()
print('mission4 complete')

# 读取csv中的数据按行展示
with open("E:/CPFS/CPFS2018/DATA/2018person.csv", "rt", encoding="utf-8") as vsvfile:
    reader = csv.reader(vsvfile)
    rows = [row for row in reader]
label_name = rows[0][0]
value_name = '%s'
row_name = rows[0][0]
for i in range(len(rows[0]) - 1):
    row_name = row_name + ' LONGTEXT, ' + rows[0][i + 1]
    label_name = label_name + ' , ' + rows[0][i + 1]
    value_name = value_name + ' , %s'

whole_name = 'CREATE TABLE CPFS2018_person(' + row_name + ' LONGTEXT) Engine=MyISAM DEFAULT CHARSET=utf8'

# 连接数据库
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='202000830046xjl',
    database='CPFS2018'
)
mycursor = mydb.cursor()

# sql = "DROP TABLE CPFS2018_person"
#
# mycursor.execute(sql)

# 新建数据表
mycursor.execute(whole_name)

# 插入数据
sql = 'INSERT INTO CPFS2018_person (' + label_name + ') VALUES (' + value_name + ')'
for i in tqdm(range(len(rows))):
    val = tuple(rows[i])
    mycursor.execute(sql, val)
    mydb.commit()
print('mission5 complete')
