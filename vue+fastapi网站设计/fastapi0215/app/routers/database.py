from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from app.models.database import *
from utils.database import select_col, col_f
import pymysql
import json
import re
import math

router = APIRouter()

VALID_CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'
database_name = {}

@router.get('/table_names')
async def table_names(Authorize: AuthJWT = Depends()):  # 生成该用户的所有表名称
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    years = ['2010', '2012', '2014', '2016', '2018']
    table_names = {}
    for year in years:
        db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + year)
        sql = "show tables"
        cursor = db.cursor()
        cursor.execute(sql)
        oneyear = {}
        k = 0
        for i in cursor.fetchall():
            if re.search(username, i[0]) and (re.search(username, i[0]).span()[1] == len(i[0])):
                k += 1
                oneyear[str(k)] = i[0].replace('_' + username, '')
        table_names[year] = oneyear
    return table_names


@router.post('/get_table')
async def Get_table(request: get_table, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    table_name = request.table_name
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps"+table_name[0:4])
    sql1 = "SELECT * FROM " + table_name + "_" + username + ";"
    cursor = db.cursor()
    cursor.execute(sql1)
    num = len(cursor.fetchall())  # 总条数
    pages = math.ceil(num / 20)  # 总页数
    col = cursor.description
    header = []
    for i in col:
        header.append(i[0])
    tableData = []
    header_eng = {}  #英文字段名
    header_cn = {}  #中文字段名
    with open("data/"+username+"/col_names.json", encoding="utf-8") as f:
        col_names = json.load(f)[table_name[0:4]][table_name]
    for key, value in col_names.items():
        flag = 1
        for i in key:
            if i not in VALID_CHARACTERS:
                flag = 0
        if flag == 0:
            header_cn[value[1]] = key
        else:
            header_eng[value[1]] = key
    tableData.append(header_eng)
    tableData.append(header_cn)
    num1 = 0
    for i in cursor:
        if num1 < 20:
            onedata = {}
            j = 0
            for k in i:
                onedata[header[j]] = k
                j += 1
            tableData.append(onedata)
        num1 += 1
    cursor.close()
    db.close()
    return {"num": num, "pages": pages, "data": tableData}


@router.post('/page1')
async def Page1(request: page1, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    table_name = request.table_name
    page = request.page
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps"+table_name[0:4])
    sql1 = "SELECT * FROM " + table_name + "_" + username + ";"
    cursor = db.cursor()
    cursor.execute(sql1)
    col = cursor.description
    header = []
    for i in col:
        header.append(i[0])
    tableData = []
    header_eng = {}  #英文字段名
    header_cn = {}  #中文字段名
    with open("data/"+username+"/col_names.json", encoding="utf-8") as f:
        col_names = json.load(f)[table_name[0:4]][table_name]
    for key, value in col_names.items():
        flag = 1
        for i in key:
            if i not in VALID_CHARACTERS:
                flag = 0
        if flag == 0:
            header_cn[value[1]] = key
        else:
            header_eng[value[1]] = key
    tableData.append(header_eng)
    tableData.append(header_cn)
    num1 = 0
    for i in cursor:
        if (num1 >= (page-1)*20) and (num1 < page * 20):
            onedata = {}
            j = 0
            for k in i:
                onedata[header[j]] = k
                j += 1
            tableData.append(onedata)
        num1 += 1
    cursor.close()
    db.close()
    return {"data": tableData}


@router.post('/curd')
async def CURD(request: curd, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    sql_code = request.sql_code
    year = None
    global database_name
    # 用户无权限创建 删除数据库、修改数据库名称
    if re.match("CREATEDATABASE|DROPDATABASE|RENAMEDATABASE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        return {"status": "failure", "reason": "抱歉，您没有权限创建、删除数据库或修改数据库名称！"}
    if re.search("RENAME", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        return {"status": "failure", "reason": "抱歉，您没有权限修改数据表名称！"}
    if re.match("CREATETABLE|ALTERTABLE|DROPTABLE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        pass
    else:
        location = re.search('201', sql_code, flags=re.IGNORECASE)
        if location:
            year = sql_code[int(location.span()[0]):int(location.span()[1]) + 1]
    # 是否为use database xxx
    if re.match("USE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        database_name[username] = re.sub('use', '', sql_code.replace(' ', '').strip(';'), flags=re.IGNORECASE)
    elif re.match("USEDATABASE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        database_name[username] = re.sub('USEDATABASE', '', sql_code.replace(' ', '').strip(';'), flags=re.IGNORECASE)
    # 替换数据表名称
    elif re.match("RENAMETABLE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        location_table = re.search("TABLE", sql_code, flags=re.IGNORECASE).span()
        location_spacing = re.finditer(" ", sql_code, flags=re.IGNORECASE)
        location1 = None
        for i in location_spacing:
            if not location1:
                if i.span()[1] > location_table[1]:
                    location1 = i.span()[1]
                    continue
            if location1:
                if i.span()[0] == location1:
                    location1 = i.span()[1]
                else:
                    location2 = i.span()[0]
                    break
        origin_table_name = sql_code[location1:location2]
        sql_code = sql_code.replace(origin_table_name, '')
        sql_code1 = list(sql_code)
        sql_code1.insert(location1, origin_table_name + '_' + username)
        sql_code = ''.join(sql_code1)
    elif re.match("DROPTABLE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        origin_table_name = re.sub('DROPTABLE', '', sql_code.replace(' ', '').strip(';'), flags=re.IGNORECASE)
        location1 = sql_code.index(origin_table_name)
        sql_code = sql_code.replace(origin_table_name, '')
        sql_code1 = list(sql_code)
        sql_code1.insert(location1, origin_table_name + '_' + username)
        sql_code = ''.join(sql_code1)
    elif re.match("SHOWTABLES", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        pass
    else:
        # 将表名称替换为表名称+用户名
        if re.search(r"[\u4E00-\u9FA5]+ ", sql_code):
            location = re.search(r"[\u4E00-\u9FA5]+ ", sql_code).span()[1] - 1
        else:
            if re.search(r"[\u4E00-\u9FA5]+[A-Za-z]+[\u4E00-\u9FA5]+", sql_code):
                location = re.search(r"[\u4E00-\u9FA5]+[A-Za-z]+[\u4E00-\u9FA5]+", sql_code).span()[1]
            else:
                location = re.search(r"[\u4E00-\u9FA5]+", sql_code).span()[1]
        sql_code1 = list(sql_code)
        sql_code1.insert(location, '_' + username)
        sql_code = ''.join(sql_code1)
    # pymysql无法执行use database xxx，记录下来即可
    if re.match("USE|USEDATABASE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        pass
    else:
        # 执行用户输入的语句
        if year:
            db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + year)
        else:
            try:
                db = pymysql.connect(host='localhost', user='root', password='zyy917382',database=database_name[username])
            except:
                return {"status": "failure", "reason": "请先选择数据库"}
        cursor = db.cursor()
        try:
            cursor.execute(sql_code)
            db.commit()
            col = cursor.description
            findall = cursor.fetchall()
        except:
            db.rollback()
            cursor.close()
            db.close()
            return {"status": "failure", "reason": "请输入正确的SQL语句"}

    # 将操作记录写入数据库
    db2 = pymysql.connect(host='localhost', user='root', password='zyy917382', database="user")
    sql0 = "SELECT sql0, sql1, sql2, sql3, sql4, sql5, sql6, sql7, sql8, sql9 FROM user WHERE name='" + username + "';"
    cursor2 = db2.cursor()
    cursor2.execute(sql0)
    records = cursor2.fetchall()[0]
    k = 0
    for record in records:
        if not record:
            break
        k += 1
    if k != 10:  # 如果还没写满
        sql2 = "UPDATE user SET sql" + str(k) + "='" + sql_code.replace("\'", '').replace("\"",'') + "' WHERE name = '" + username + "';"
    else:  # 如果已经写满了，则删除最早的记录
        newrecord = []
        k = 0
        for record in records:
            if k != 0:
                newrecord.append(record)
            k += 1
        sql2 = "UPDATE user SET sql0='" + newrecord[0] + "',sql1='" + newrecord[1] + "',sql2='" + newrecord[2] + "',sql3='" + newrecord[3] + "',sql4='" + newrecord[4] + "',sql5='" + newrecord[5] + "',sql6='" + newrecord[6] + "',sql7='" + newrecord[7] + "',sql8='" + newrecord[8] + "',sql9='" + sql_code.replace("\'", '').replace("\"", '') + "' WHERE name = '" + username + "';"

    if re.match("CREATETABLE", sql_code.replace(' ', ''), flags=re.IGNORECASE) and re.search("SELECT",sql_code.replace(' ', ''),flags=re.IGNORECASE):
        location1 = re.match('CREATETABLE', sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[1]
        location2 = re.search('SELECT', sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[0]
        table_name = sql_code.replace(' ', '')[location1:location2]
        sql3 = "SELECT * FROM " + table_name + ";"
        cursor.execute(sql3)
        new_col_names = {}
        for i in cursor.description:
            new_col_names[i[0]] = [i[0], i[0]]
        with open("data/" + username + "/col_names.json", encoding="utf-8") as f:
            col_names = json.load(f)
        col_names[database_name[username][4:8]][table_name] = new_col_names
        fb = open("data/" + username + "/col_names.json", 'w', encoding='utf-8')
        fb.write(json.dumps(col_names, ensure_ascii=False, indent=2))
        fb.close()
        cursor.close()
        db.close()
        try:
            cursor2.execute(sql2)
            db2.commit()
            cursor2.close()
            db2.close()
            return {"status": "success"}
        except:
            cursor2.close()
            db2.close()
            return {"status": "failure", "reason": "无法执行该语句"}
    if re.match("CREATETABLE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        if re.match('CREATETABLEIFNOTEXISTS', sql_code.replace(' ', ''), flags=re.IGNORECASE):
            location1 = re.match('CREATETABLEIFNOTEXISTS', sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[1]
        else:
            location1 = re.match("CREATETABLE", sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[1]
        location2 = re.search('\\(', sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[0]
        table_name = sql_code.replace(' ', '')[location1:location2]
        sql3 = "SELECT * FROM " + table_name + ";"
        cursor.execute(sql3)
        new_col_names = {}
        for i in cursor.description:
            new_col_names[i[0]] = [i[0], i[0]]
        with open("data/" + username + "/col_names.json", encoding="utf-8") as f:
            col_names = json.load(f)
        col_names[database_name[username][4:8]][table_name] = new_col_names
        fb = open("data/" + username + "/col_names.json", 'w', encoding='utf-8')
        fb.write(json.dumps(col_names, ensure_ascii=False, indent=2))
        fb.close()
        cursor.close()
        db.close()
        try:
            cursor2.execute(sql2)
            db2.commit()
            cursor2.close()
            db2.close()
            return {"status": "success"}
        except:
            cursor2.close()
            db2.close()
            return {"status": "failure", "reason": "无法执行该语句"}
    if re.match("DROPTABLE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        if re.match('DROPTABLEIFEXISTS', sql_code.replace(' ', ''), flags=re.IGNORECASE):
            table_name = re.sub('DROPTABLEIFEXISTS', '', sql_code.replace(' ', '').strip(';'), flags=re.IGNORECASE)
        else:
            table_name = re.sub('DROPTABLE', '', sql_code.replace(' ', '').strip(';'), flags=re.IGNORECASE)
        with open("data/" + username + "/col_names.json", encoding="utf-8") as f:
            col_names = json.load(f)
        del col_names[database_name[username][4:8]][table_name]
        fb = open("data/" + username + "/col_names.json", 'w', encoding='utf-8')
        fb.write(json.dumps(col_names, ensure_ascii=False, indent=2))
        fb.close()
        cursor.close()
        db.close()
        try:
            cursor2.execute(sql2)
            db2.commit()
            cursor2.close()
            db2.close()
            return {"status": "success"}
        except:
            cursor2.close()
            db2.close()
            return {"status": "failure", "reason": "无法执行该语句"}
    if re.match("RENAME", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        location1 = re.match("RENAMETABLE", sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[1]
        location2 = re.search("TO", sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[0]
        location3 = re.search("TO", sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[1]
        old_table_name = sql_code.replace(' ', '')[location1:location2]
        new_table_name = sql_code.replace(' ', '').replace(';', '')[location3:]
        with open("data/" + username + "/col_names.json", encoding="utf-8") as f:
            col_names = json.load(f)
        col_names[database_name[username][4:8]][new_table_name] = col_names[database_name[username][4:8]][
            old_table_name]
        del col_names[database_name[username][4:8]][old_table_name]
        fb = open("data/" + username + "/col_names.json", 'w', encoding='utf-8')
        fb.write(json.dumps(col_names, ensure_ascii=False, indent=2))
        fb.close()
        cursor.close()
        db.close()
        try:
            cursor2.execute(sql2)
            db2.commit()
            cursor2.close()
            db2.close()
            return {"status": "success"}
        except:
            cursor2.close()
            db2.close()
            return {"status": "failure", "reason": "无法执行该语句"}
    if re.match("ALTERTABLE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        location1 = re.match('ALTERTABLE', sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[1]
        if re.search("ADD", sql_code.replace(' ', ''), flags=re.IGNORECASE):
            location2 = re.search('ADD', sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[0]
            table_name = sql_code.replace(' ', '')[location1:location2]
        elif re.search("DROP", sql_code.replace(' ', ''), flags=re.IGNORECASE):
            location2 = re.search('DROP', sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[0]
            table_name = sql_code.replace(' ', '')[location1:location2]
        elif re.search("CHANGE", sql_code.replace(' ', ''), flags=re.IGNORECASE):
            location2 = re.search('CHANGE', sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[0]
            table_name = sql_code.replace(' ', '')[location1:location2]
        elif re.search("MODIFY", sql_code.replace(' ', ''), flags=re.IGNORECASE):
            location2 = re.search('MODIFY', sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[0]
            table_name = sql_code.replace(' ', '')[location1:location2]
        elif re.search("RENAME", sql_code.replace(' ', ''), flags=re.IGNORECASE):
            location2 = re.search('RENAME', sql_code.replace(' ', ''), flags=re.IGNORECASE).span()[0]
            table_name = sql_code.replace(' ', '').replace(';', '')[location2:]
        sql3 = "SELECT * FROM " + table_name + ";"
        cursor.execute(sql3)
        new_col_names = {}
        for i in cursor.description:
            new_col_names[i[0]] = [i[0], i[0]]
        with open("data/" + username + "/col_names.json", encoding="utf-8") as f:
            col_names = json.load(f)
        col_names[database_name[username][4:8]][table_name] = new_col_names
        fb = open("data/" + username + "/col_names.json", 'w', encoding='utf-8')
        fb.write(json.dumps(col_names, ensure_ascii=False, indent=2))
        fb.close()
        cursor.close()
        db.close()
        try:
            cursor2.execute(sql2)
            db2.commit()
            cursor2.close()
            db2.close()
            return {"status": "success"}
        except:
            cursor2.close()
            db2.close()
            return {"status": "failure", "reason": "无法执行该语句"}
    if re.match("SELECT", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        header = []
        for i in col:
            header.append(i[0])
        tableData = []
        header2 = {}
        for i in header:
            header2[i] = i
        tableData.append(header2)
        num = len(findall)  # 总条数
        pages = math.ceil(num / 20)  # 总页数
        num1 = 0
        for i in findall:
            if num1 < 20:
                onedata = {}
                j = 0
                for k in i:
                    onedata[header[j]] = k
                    j += 1
                tableData.append(onedata)
            else:
                break
            num1 += 1
        integration = {"status": "success", "num": num, "pages": pages, "data": tableData}
        try:
            cursor2.execute(sql2)
            db2.commit()
            cursor2.close()
            db2.close()
            return integration
        except:
            cursor2.close()
            db2.close()
            return {"status": "failure", "reason": "无法执行该语句"}
    if re.match("SHOWTABLES", sql_code.replace(' ', ''), flags=re.IGNORECASE):
        num = 0
        tableData = []
        for table in findall:
            if re.search(username, table[0]) and (re.search(username, table[0]).span()[1] == len(table[0])):
                tableData.append({"表格名称": re.sub('_' + username, '', table[0])})
                num += 1
        pages = math.ceil(num / 20)  # 总页数
        integration = {"status": "success", "num": num, "pages": pages, "data": tableData}
        try:
            cursor2.execute(sql2)
            db2.commit()
            cursor2.close()
            db2.close()
            return integration
        except:
            cursor2.close()
            db2.close()
            return {"status": "failure", "reason": "无法执行该语句"}
    else:
        try:
            cursor2.execute(sql2)
            db2.commit()
            cursor2.close()
            db2.close()
            return {"status": "success"}
        except:
            cursor2.close()
            db2.close()
            return {"status": "failure", "reason": "无法执行该语句"}


@router.post('/page2')
async def Page2(request: page2, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    sql_code = request.sql_code
    page = request.page
    location = re.search('201', sql_code, flags=re.IGNORECASE)
    if location:
        year = sql_code[int(location.span()[0]):int(location.span()[1]) + 1]
    # 将表名称替换为表名称+用户名
    if re.search(r"[\u4E00-\u9FA5]+ ", sql_code):
        location = re.search(r"[\u4E00-\u9FA5]+ ", sql_code).span()[1] - 1
    else:
        if re.search(r"[\u4E00-\u9FA5]+[A-Za-z]+[\u4E00-\u9FA5]+", sql_code):
            location = re.search(r"[\u4E00-\u9FA5]+[A-Za-z]+[\u4E00-\u9FA5]+", sql_code).span()[1]
        else:
            location = re.search(r"[\u4E00-\u9FA5]+", sql_code).span()[1]
    sql_code1 = list(sql_code)
    sql_code1.insert(location, '_' + username)
    sql_code = ''.join(sql_code1)
    try:
        db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + year)
    except:
        global database_name
        db = pymysql.connect(host='localhost', user='root', password='zyy917382', database=database_name[username])
    cursor = db.cursor()
    cursor.execute(sql_code)
    col = cursor.description
    findall = cursor.fetchall()
    header = []
    for i in col:
        header.append(i[0])
    tableData = []
    header2 = {}
    for i in header:
        header2[i] = i
    tableData.append(header2)
    num1 = 0
    for i in findall:
        if (num1 >= (page-1)*20) and (num1 < page * 20):
            onedata = {}
            j = 0
            for k in i:
                onedata[header[j]] = k
                j += 1
            tableData.append(onedata)
        num1 += 1
    integration = {"status": "success", "data": tableData}
    cursor.close()
    db.close()
    return integration


@router.get('/get_records')
async def Get_record(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="user")
    sql = "SELECT sql0, sql1, sql2, sql3, sql4, sql5, sql6, sql7, sql8, sql9 FROM user WHERE name='" + username + "';"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    records = []
    for record in cursor.fetchall()[0]:
        if record:
            records.append(re.sub('_'+username, '', record))
    return {"status": "success", "records": records}


@router.get('/col_names')
async def col_names(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    with open("data/"+username+"/col_names.json", encoding="utf-8") as f:
        col_names = json.load(f)
    return col_names


@router.post('/get_cols')
async def Get_cols(request: get_cols, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    tip = request.tip
    table1 = tip["tubiao1"]
    table2 = tip["tubiao2"]
    table3 = tip["tubiao3"]
    with open("data/"+username+"/col_names.json", encoding="utf-8") as f:
        col_names = json.load(f)
    if table1 != "1":
        col1 = col_names[table1[0:4]][table1]
        col1_ = col_f(col1)
    else:
        col1_ = "1"
    if table2 != "1":
        col2 = col_names[table2[0:4]][table2]
        col2_ = col_f(col2)
    else:
        col2_ = "1"
    if table3 != "1":
        col3 = col_names[table3[0:4]][table3]
        col3_ = col_f(col3)
    else:
        col3_ = "1"
    res = {"tubiao1": col1_, "tubiao2": col2_, "tubiao3": col3_}
    return res


@router.post('/select_cols')
async def Select_cols(request: select_cols, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    tip = request.tip
    table1 = tip["tubiao1"]
    table2 = tip["tubiao2"]
    table3 = tip["tubiao3"]
    col1_cn = tip["biaoqian1"]
    col2_cn = tip["biaoqian2"]
    col3_cn = tip["biaoqian3"]
    with open("data/"+username+"/col_names.json", encoding="utf-8") as f:
        col_names = json.load(f)
    col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
    res1 = select_col(table1, col1_eng, username, 1)
    num1 = res1["num"]
    pages1 = res1["pages"]
    del res1["num"]
    del res1["pages"]
    if table2 != '1':
        col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
        res2 = select_col(table2, col2_eng, username, 1)
        num2 = res2["num"]
        pages2 = res2["pages"]
        del res2["num"]
        del res2["pages"]
        if table3 != '1':
            col3_eng = col_names[table3[0:4]][table3][col3_cn][1]
            res3 = select_col(table3, col3_eng, username, 1)
            num3 = res3["num"]
            pages3 = res3["pages"]
            del res3["num"]
            del res3["pages"]
            num = min(num1, num2, num3)
            pages = min(pages1, pages2, pages3)
        else:
            res3 = '1'
            num = min(num1, num2)
            pages = min(pages1, pages2)
    else:
        res2 = '1'
        res3 = '1'
        num = num1
        pages = pages1
    integration = {"num": num, "pages": pages, "biaoqian1": res1, "biaoqian2": res2, "biaoqian3": res3}
    return integration


@router.post('/page3')
async def Page3(request: page3, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    page = request.page
    tip = request.tip
    table1 = tip["tubiao1"]
    table2 = tip["tubiao2"]
    table3 = tip["tubiao3"]
    col1_cn = tip["biaoqian1"]
    col2_cn = tip["biaoqian2"]
    col3_cn = tip["biaoqian3"]
    with open("data/"+username+"/col_names.json", encoding="utf-8") as f:
        col_names = json.load(f)
    if table1 != '1':
        col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
        res1 = select_col(table1, col1_eng, username, page)
        del res1["num"]
        del res1["pages"]
    else:
        res1 = '1'
    if table2 != '1':
        col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
        res2 = select_col(table2, col2_eng, username, page)
        del res2["num"]
        del res2["pages"]
    else:
        res2 = '1'
    if table3 != '1':
        col3_eng = col_names[table3[0:4]][table3][col3_cn][1]
        res3 = select_col(table3, col3_eng, username, 1)
        del res3["num"]
        del res3["pages"]
    else:
        res3 = '1'
    integration = {"biaoqian1": res1, "biaoqian2": res2, "biaoqian3": res3}
    return integration