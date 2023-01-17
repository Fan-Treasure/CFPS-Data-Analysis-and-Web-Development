from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.dialects.mysql import LONGTEXT
import mysql.connector
import csv
from tqdm import tqdm

# 读取csv中的数据按行展示
with open("E:/CPFS/CPFS2014/DATA/2014adult.csv", "rt", encoding="utf-8") as vsvfile:
    reader = csv.reader(vsvfile)
    rows = [row for row in reader]
label_name = rows[0][0]
value_name = '%s'
row_name = rows[0][0]
for i in range(len(rows[0]) - 1):
    row_name = row_name + ' LONGTEXT, ' + rows[0][i + 1]
    label_name = label_name + ' , ' + rows[0][i + 1]
    value_name = value_name + ' , %s'

whole_name = 'CREATE TABLE CPFS2014_adult (' + row_name + ' LONGTEXT) Engine=MyISAM DEFAULT CHARSET=utf8'

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='CPFS2014'
)
mycursor = mydb.cursor()

# sql = "DROP TABLE CPFS2014_adult"
#
# mycursor.execute(sql)

# 新建数据表
mycursor.execute(whole_name)

# 插入数据
sql = 'INSERT INTO CPFS2014_adult (' + label_name + ') VALUES (' + value_name + ')'
for i in tqdm(range(len(rows))):
    val = tuple(rows[i])
    mycursor.execute(sql, val)
    mydb.commit()
print('mission1 complete')

# 读取csv中的数据按行展示
with open("E:/CPFS/CPFS2014/DATA/2014child.csv", "rt", encoding="utf-8") as vsvfile:
    reader = csv.reader(vsvfile)
    rows = [row for row in reader]
label_name = rows[0][0]
value_name = '%s'
row_name = rows[0][0]
for i in range(len(rows[0]) - 1):
    row_name = row_name + ' LONGTEXT, ' + rows[0][i + 1]
    label_name = label_name + ' , ' + rows[0][i + 1]
    value_name = value_name + ' , %s'

whole_name = 'CREATE TABLE CPFS2014_child (' + row_name + ' LONGTEXT) Engine=MyISAM DEFAULT CHARSET=utf8'

# 连接数据库
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='202000830046xjl',
    database='CPFS2014'
)
mycursor = mydb.cursor()

# sql = "DROP TABLE CPFS2014_child"
#
# mycursor.execute(sql)

# 新建数据表
mycursor.execute(whole_name)

# 插入数据
sql = 'INSERT INTO CPFS2014_child (' + label_name + ') VALUES (' + value_name + ')'
for i in tqdm(range(len(rows))):
    val = tuple(rows[i])
    mycursor.execute(sql, val)
    mydb.commit()
print('mission2 complete')

# 读取csv中的数据按行展示
with open("E:/CPFS/CPFS2014/DATA/2014common.csv", "rt", encoding="utf-8") as vsvfile:
    reader = csv.reader(vsvfile)
    rows = [row for row in reader]
label_name = rows[0][0]
value_name = '%s'
row_name = rows[0][0]
for i in range(len(rows[0]) - 1):
    row_name = row_name + ' LONGTEXT, ' + rows[0][i + 1]
    label_name = label_name + ' , ' + rows[0][i + 1]
    value_name = value_name + ' , %s'

whole_name = 'CREATE TABLE CPFS2014_common (' + row_name + ' LONGTEXT) Engine=MyISAM DEFAULT CHARSET=utf8'

# 连接数据库
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='202000830046xjl',
    database='CPFS2014'
)
mycursor = mydb.cursor()

# sql = "DROP TABLE CPFS2014_common"
#
# mycursor.execute(sql)

# 新建数据表
mycursor.execute(whole_name)

# 插入数据
sql = 'INSERT INTO CPFS2014_common (' + label_name + ') VALUES (' + value_name + ')'
for i in tqdm(range(len(rows))):
    val = tuple(rows[i])
    mycursor.execute(sql, val)
    mydb.commit()
print('mission3 complete')

# 读取csv中的数据按行展示
with open("E:/CPFS/CPFS2014/DATA/2014famconf.csv", "rt", encoding="utf-8") as vsvfile:
    reader = csv.reader(vsvfile)
    rows = [row for row in reader]
label_name = rows[0][0]
value_name = '%s'
row_name = rows[0][0]
for i in range(len(rows[0]) - 1):
    row_name = row_name + ' LONGTEXT, ' + rows[0][i + 1]
    label_name = label_name + ' , ' + rows[0][i + 1]
    value_name = value_name + ' , %s'

whole_name = 'CREATE TABLE CPFS2014_famconf(' + row_name + ' LONGTEXT) Engine=MyISAM DEFAULT CHARSET=utf8'

# 连接数据库
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='202000830046xjl',
    database='CPFS2014'
)
mycursor = mydb.cursor()

# sql = "DROP TABLE CPFS2014_famconf"
#
# mycursor.execute(sql)

# 新建数据表
mycursor.execute(whole_name)

# 插入数据
sql = 'INSERT INTO CPFS2014_famconf (' + label_name + ') VALUES (' + value_name + ')'
for i in tqdm(range(len(rows))):
    val = tuple(rows[i])
    mycursor.execute(sql, val)
    mydb.commit()
print('mission4 complete')

# 读取csv中的数据按行展示
with open("E:/CPFS/CPFS2014/DATA/2014famecon.csv", "rt", encoding="utf-8") as vsvfile:
    reader = csv.reader(vsvfile)
    rows = [row for row in reader]
label_name = rows[0][0]
value_name = '%s'
row_name = rows[0][0]
for i in range(len(rows[0]) - 1):
    row_name = row_name + ' LONGTEXT, ' + rows[0][i + 1]
    label_name = label_name + ' , ' + rows[0][i + 1]
    value_name = value_name + ' , %s'

whole_name = 'CREATE TABLE CPFS2014_famecon(' + row_name + ' LONGTEXT) Engine=MyISAM DEFAULT CHARSET=utf8'

# 连接数据库
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='202000830046xjl',
    database='CPFS2014'
)
mycursor = mydb.cursor()

# sql = "DROP TABLE CPFS2014_famecon"
#
# mycursor.execute(sql)

# 新建数据表
mycursor.execute(whole_name)

# 插入数据
sql = 'INSERT INTO CPFS2014_famecon (' + label_name + ') VALUES (' + value_name + ')'
for i in tqdm(range(len(rows))):
    val = tuple(rows[i])
    mycursor.execute(sql, val)
    mydb.commit()
print('mission5 complete')
