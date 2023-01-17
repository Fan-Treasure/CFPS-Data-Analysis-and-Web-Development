import mysql.connector
import csv
import os
from tqdm import tqdm


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

num = 2010
whole_path = 'F:/数据库数据/CPFS/CPFS数据/CPFS'+str(num)+'/数据已清洗/'
for root, dirs, files in os.walk(whole_path):
    print(root)
for sig in range(len(files)):
    csv_name = whole_path + files[sig]

    # 读取csv中的数据按行展示
    with open(csv_name, "rt", encoding="gbk") as vsvfile:
        reader = csv.reader(vsvfile)
        rows = [row for row in reader]
    label_name = rows[0][0]
    value_name = '%s'
    row_name = rows[0][0]
    if (is_number(rows[1][0])):
        row_name = row_name + ' INT, '
    else:
        row_name = row_name + ' LONGTEXT, '
    for i in range(len(rows[0]) - 1):
        label_name = label_name + ' , ' + rows[0][i + 1]
        value_name = value_name + ' , %s'
        if (is_number(rows[1][i + 1])):
            row_name = row_name + rows[0][i + 1] + ' INT, '
        else:
            row_name = row_name + rows[0][i + 1] + ' LONGTEXT, '
    row_name_final = row_name[:-2]
    whole_name = 'CREATE TABLE '+files[sig][0:4]+' (' + row_name_final + ' ) Engine=MyISAM DEFAULT CHARSET=utf8'
    # 连接数据库
    mydb = mysql.connector.connect(
        host='',
        user='',
        password='',
        database='CPFS2010'
    )
    mycursor = mydb.cursor()

    # sql = "DROP TABLE "+files[sig][0:4]
    #
    # mycursor.execute(sql)
    # 新建数据表
    mycursor.execute(whole_name)

    # 插入数据
    sql = 'INSERT INTO '+files[sig][0:4]+' (' + label_name + ') VALUES (' + value_name + ')'
    for i in tqdm(range(len(rows) - 1)):
        if (is_number(rows[i + 1][0])):
            val = [float(rows[i + 1][0])]
        else:
            val = [rows[i + 1][0]]
        for j in range(len(rows[0]) - 1):
            if (is_number(rows[i + 1][j + 1])):
                val.append(float(rows[i + 1][j + 1]))
            else:
                val.append(rows[i + 1][j + 1])

        mycursor.execute(sql, val)
        mydb.commit()
    print('mission '+str(sig+1)+' complete')




