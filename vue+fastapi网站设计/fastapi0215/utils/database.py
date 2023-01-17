import pymysql
import re
import math

VALID_CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'

def select_col(table: str, col: str, username: str, page: int):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql1 = "SELECT " + col + " FROM " + table + "_" + username + ";"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    tableData = []
    all = cursor.fetchall()
    num = len(all)
    pages = math.ceil(num/20)
    num1 = 0
    for i in all:
        if (num1 >= (page-1)*20) and (num1 < page * 20):
            for k in i:
                tableData.append(k)
        num1 += 1
    cursor = db.cursor()
    sql2 = "SELECT " + col + ", COUNT(*) FROM " + table + " GROUP BY " + col + " ;"
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    rawdata = cursor.fetchall()
    if len(rawdata) > 10:
        type = 'a'
    else:
        type = 'b'
    cursor.close()
    db.close()
    return {"name": col, "type": type, "data": tableData, "num": num, "pages": pages}

'''
def strornum(input: str):
    try:
        int(input)
        return 'num'
    except:
        return 'str'
'''

def col_f(col: dict):  #转一列数据的格式
    col_ = []
    for key, value in col.items():
        flag = 1
        for i in key:
            if i not in VALID_CHARACTERS:
                flag = 0
        if flag == 0:
            col_.append(key)
    return col_


def copy_database(username: str):  # 为新用户复制数据库
    years = ['2010', '2012', '2014', '2016', '2018']
    for year in years:
        db = pymysql.connect(host='localhost', user='root', password='zyy917382', database='cfps'+year)
        sql0 = "show tables;"
        cursor = db.cursor()
        cursor.execute(sql0)
        for table in cursor.fetchall():
            if not re.search('_', table[0]):
                sql1 = "CREATE TABLE " + table[0] + "_" + username + " SELECT * FROM " + table[0] + ";"
                cursor.execute(sql1)