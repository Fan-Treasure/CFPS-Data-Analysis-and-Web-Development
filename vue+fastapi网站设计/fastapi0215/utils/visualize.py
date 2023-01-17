import pymysql
import numpy as np
import math


letters = 'abcdefghijklmnopqrstuvwxyz'

def a_ns_count12345(table: str, col: str, tubiao: str, username: str):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql1 = "SELECT SUM(" + col + ") FROM " + table + "_" + username + " WHERE (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql2 = "SELECT SUM(" + col + ") FROM " + table + "_" + username + " WHERE (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql3 = "SELECT SUM(" + col + ") FROM " + table + "_" + username + " WHERE (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    sql4 = "SELECT SUM(" + col + ") FROM " + table + "_" + username + " WHERE (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_c_sum = cursor.fetchall()[0][0]  #北方城镇总和
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_v_sum = cursor.fetchall()[0][0]  #北方乡村总和
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_c_sum = cursor.fetchall()[0][0]  # 南方城镇总和
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_v_sum = cursor.fetchall()[0][0]  # 南方乡村总和
    sql5 = "SELECT COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql6 = "SELECT COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql7 = "SELECT COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    sql8 = "SELECT COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_c_count = cursor.fetchall()[0][0]  # 北方城镇总数
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_v_count = cursor.fetchall()[0][0]  # 北方乡村总数
    try:
        cursor.execute(sql7)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_c_count = cursor.fetchall()[0][0]  # 南方城镇总数
    try:
        cursor.execute(sql8)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_v_count = cursor.fetchall()[0][0]  # 南方乡村总数
    try:
        n_c_portion = round(n_c_sum/n_c_count, 2)
    except:
        n_c_portion = 0
    try:
        n_v_portion = round(n_v_sum/n_v_count, 2)
    except:
        n_v_portion = 0
    try:
        s_c_portion = round(s_c_sum/s_c_count, 2)
    except:
        s_c_portion = 0
    try:
        s_v_portion = round(s_v_sum/s_v_count, 2)
    except:
        s_v_portion = 0
    if tubiao == '1' or tubiao == '2' or tubiao == '3' or tubiao == '5' or tubiao == '25':
        return {"header": ["北方城镇", "北方农村", "南方城镇", "南方农村"],
                "data": [n_c_portion, n_v_portion, s_c_portion, s_v_portion]}
    if tubiao == '4':
        max0 = math.ceil(1.1 * max(n_c_portion, n_v_portion, s_c_portion, s_v_portion))
        return {"header": ["北方城镇", "北方农村", "南方城镇", "南方农村"],
                "data": [n_c_portion, n_v_portion, s_c_portion, s_v_portion],
                "max": max0}

def a_ecw_count12345(table: str, col: str, tubiao: str, username: str):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql1 = "SELECT SUM(" + col + ") FROM " + table + "_" + username + " WHERE (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql2 = "SELECT SUM(" + col + ") FROM " + table + "_" + username + " WHERE (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql3 = "SELECT SUM(" + col + ") FROM " + table + "_" + username + " WHERE (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql4 = "SELECT SUM(" + col + ") FROM " + table + "_" + username + " WHERE (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql5 = "SELECT SUM(" + col + ") FROM " + table + "_" + username + " WHERE (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    sql6 = "SELECT SUM(" + col + ") FROM " + table + "_" + username + " WHERE (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_c_sum = cursor.fetchall()[0][0]  # 东部城镇总和
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_v_sum = cursor.fetchall()[0][0]  # 东部乡村总和
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_c_sum = cursor.fetchall()[0][0]  # 中部城镇总和
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_v_sum = cursor.fetchall()[0][0]  # 中部乡村总和
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_c_sum = cursor.fetchall()[0][0]  # 西部城镇总和
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_v_sum = cursor.fetchall()[0][0]  # 西部乡村总和
    sql7 = "SELECT COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql8 = "SELECT COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql9 = "SELECT COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql10 = "SELECT COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql11 = "SELECT COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    sql12 = "SELECT COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    try:
        cursor.execute(sql7)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_c_count = cursor.fetchall()[0][0]  # 东部城镇总数
    try:
        cursor.execute(sql8)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_v_count = cursor.fetchall()[0][0]  # 东部乡村总数
    try:
        cursor.execute(sql9)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_c_count = cursor.fetchall()[0][0]  # 中部城镇总数
    try:
        cursor.execute(sql10)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_v_count = cursor.fetchall()[0][0]  # 中部乡村总数
    try:
        cursor.execute(sql11)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_c_count = cursor.fetchall()[0][0]  # 西部城镇总数
    try:
        cursor.execute(sql12)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_v_count = cursor.fetchall()[0][0]  # 西部乡村总数
    try:
        e_c_portion = round(e_c_sum/e_c_count, 2)
    except:
        e_c_portion = 0
    try:
        e_v_portion = round(e_v_sum / e_v_count, 2)
    except:
        e_v_portion = 0
    try:
        c_c_portion = round(c_c_sum/c_c_count, 2)
    except:
        c_c_portion = 0
    try:
        c_v_portion = round(c_v_sum / c_v_count, 2)
    except:
        c_v_portion = 0
    try:
        w_c_portion = round(w_c_sum/w_c_count, 2)
    except:
        w_c_portion = 0
    try:
        w_v_portion = round(w_v_sum / w_v_count, 2)
    except:
        w_v_portion = 0
    if tubiao == '1' or tubiao == '2' or tubiao == '3' or tubiao == '5' or tubiao == '25':
        return {"header": ["东部城镇", "东部农村", "中部城镇", "中部农村", "西部城镇", "西部农村"],
                "data": [e_c_portion, e_v_portion, c_c_portion, c_v_portion, w_c_portion, w_v_portion]}
    if tubiao == '4':
        max0 = math.ceil(1.1 * max(e_c_portion, e_v_portion, c_c_portion, c_v_portion, w_c_portion, w_v_portion))
        return {"header": ["东部城镇", "东部农村", "中部城镇", "中部农村", "西部城镇", "西部农村"],
                "data": [e_c_portion, e_v_portion, c_c_portion, c_v_portion, w_c_portion, w_v_portion],
                "max": max0}



def tuple2dict8(tuple: tuple):
    dict = {}
    for i in tuple:
        dict[i[0]] = i[1]
    for key, value in dict.items():
        dict[key] = value
    return dict

def b_ns_count8(table: str, col: str, username: str):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') group by " + col + ";"
    sql1 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区') group by " + col + ";"
    sql2 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区') group by " + col + ";"
    sql3 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省') group by " + col + ";"
    sql4 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and "+ col +" != '不知道' and "+ col +" != '拒绝回答' and "+ col +" != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省') group by " + col + ";"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = tuple2dict8(cursor.fetchall())  # 全部
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_c_count = tuple2dict8(cursor.fetchall())  # 北方城镇
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_v_count = tuple2dict8(cursor.fetchall())  # 北方乡村
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_c_count = tuple2dict8(cursor.fetchall())  # 南方城镇
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_v_count = tuple2dict8(cursor.fetchall())  # 南方乡村
    portion = {}
    for key, value in total.items():
        try:
            n_c = n_c_count[key]
        except:
            n_c = 0
        try:
            n_v = n_v_count[key]
        except:
            n_v = 0
        try:
            s_c = s_c_count[key]
        except:
            s_c = 0
        try:
            s_v = s_v_count[key]
        except:
            s_v = 0
        portion[key] = [n_c, n_v, s_c, s_v]
    res = {"header": ["北方城镇", "北方农村", "南方城镇", "南方农村"]}
    k = 0
    for key, value in portion.items():
        res['a'+str(k)] = {"name": key, "data": value}
        k += 1
    flag = 0
    while flag == 0:
        if k < 8:
            res['a' + str(k)] = {"name": "", "data": []}
            k += 1
        else:
            flag = 1
    return res

def b_ecw_count8(table: str, col: str, username: str):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " group by " + col + ";"
    sql1 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省') group by " + col + ";"
    sql2 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省') group by " + col + ";"
    sql3 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省') group by " + col + ";"
    sql4 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省') group by " + col + ";"
    sql5 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区') group by " + col + ";"
    sql6 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区') group by " + col + ";"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = tuple2dict8(cursor.fetchall())  # 全部
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_c_count = tuple2dict8(cursor.fetchall())  # 东部城镇
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_v_count = tuple2dict8(cursor.fetchall())  # 东部乡村
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_c_count = tuple2dict8(cursor.fetchall())  # 中部城镇
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_v_count = tuple2dict8(cursor.fetchall())  # 中部乡村
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_c_count = tuple2dict8(cursor.fetchall())  # 西部城镇
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_v_count = tuple2dict8(cursor.fetchall())  # 西部乡村
    portion = {}
    for key, value in total.items():
        try:
            e_c = e_c_count[key]
        except:
            e_c = 0
        try:
            e_v = e_v_count[key]
        except:
            e_v = 0
        try:
            c_c = c_c_count[key]
        except:
            c_c = 0
        try:
            c_v = c_v_count[key]
        except:
            c_v = 0
        try:
            w_c = w_c_count[key]
        except:
            w_c = 0
        try:
            w_v = w_v_count[key]
        except:
            w_v = 0
        portion[key] = [e_c, e_v, c_c, c_v, w_c, w_v]
    res = {"header": ["东部城镇", "东部农村", "中部城镇", "中部农村", "西部城镇", "西部农村"]}
    k = 0
    for key, value in portion.items():
        res['a'+str(k)] = {"name": key, "data": value}
        k += 1
    flag = 0
    while flag == 0:
        if k < 8:
            res['a' + str(k)] = {"name": "", "data": []}
            k += 1
        else:
            flag = 1
    return res



def tuple2list91011a(tuple: tuple):
    list = []
    for i in tuple:
        list.append(float(i[0]))
    return list

def count_quantiles(tuple: tuple, quantiles: list):  # 根据四分位数统计个数
    first = second = third = fourth = 0
    for i in tuple:
        if float(i[0]) <= quantiles[0]:
            first += 1
        if (float(i[0]) > quantiles[0]) and (float(i[0]) <= quantiles[1]):
            second += 1
        if (float(i[0]) > quantiles[1]) and (float(i[0]) <= quantiles[2]):
            third += 1
        if float(i[0]) > quantiles[2]:
            fourth += 1
    return [{'value': first, 'name': '0—'+str(quantiles[0])},
            {'value': second, 'name': str(quantiles[0])+'—'+str(quantiles[1])},
            {'value': third, 'name': str(quantiles[1])+'—'+str(quantiles[2])},
            {'value': fourth, 'name': str(quantiles[2])+'—'+str(quantiles[3])}]

def a_ns_count91011(table: str, col: str, username: str):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0');"
    sql1 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql2 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql3 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    sql4 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = cursor.fetchall()
    total2 = tuple2list91011a(total)  # 全部
    quantiles = np.percentile(total2, (25, 50, 75))
    quantiles = [float(quantiles[0]), float(quantiles[1]), float(quantiles[2])]
    quantiles.append(max(total2))
    total_count = count_quantiles(total, quantiles)  # 总体四部分各有多少
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_c_all = cursor.fetchall()  # 北方城镇全部数据
    n_c_count = count_quantiles(n_c_all, quantiles)  # 北方城镇四部分各有多少
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_v_all = cursor.fetchall()  # 北方乡村全部数据
    n_v_count = count_quantiles(n_v_all, quantiles)  # 北方乡村四部分各有多少
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_c_all = cursor.fetchall()  # 南方城镇全部数据
    s_c_count = count_quantiles(s_c_all, quantiles)  # 南方城镇四部分各有多少
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_v_all = cursor.fetchall()  # 南方乡村全部数据
    s_v_count = count_quantiles(s_v_all, quantiles)  # 南方乡村四部分各有多少
    return {'总体': total_count, '北方城镇': n_c_count, '北方农村': n_v_count, '南方城镇': s_c_count, '南方农村': s_v_count}

def a_ecw_count91011(table: str, col: str, username: str):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0');"
    sql1 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql2 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql3 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql4 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql5 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    sql6 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = cursor.fetchall()
    total2 = tuple2list91011a(total)  # 全部
    quantiles = np.percentile(total2, (25, 50, 75))
    quantiles = [float(quantiles[0]), float(quantiles[1]), float(quantiles[2])]
    quantiles.append(max(total2))
    total_count = count_quantiles(total, quantiles)  # 总体四部分各有多少
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_c_all = cursor.fetchall()  # 东部城镇全部数据
    e_c_count = count_quantiles(e_c_all, quantiles)  # 东部城镇四部分各有多少
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_v_all = cursor.fetchall()  # 东部乡村全部数据
    e_v_count = count_quantiles(e_v_all, quantiles)  # 东部乡村四部分各有多少
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_c_all = cursor.fetchall()  # 中部城镇全部数据
    c_c_count = count_quantiles(c_c_all, quantiles)  # 中部城镇四部分各有多少
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_v_all = cursor.fetchall()  # 中部乡村全部数据
    c_v_count = count_quantiles(c_v_all, quantiles)  # 中部乡村四部分各有多少
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_c_all = cursor.fetchall()  # 西部城镇全部数据
    w_c_count = count_quantiles(w_c_all, quantiles)  # 西部城镇四部分各有多少
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_v_all = cursor.fetchall()  # 西部乡村全部数据
    w_v_count = count_quantiles(w_v_all, quantiles)  # 西部乡村四部分各有多少
    return {'总体': total_count, '东部城镇': e_c_count, '东部农村': e_v_count, '中部城镇': c_c_count, '中部农村': c_v_count, '西部城镇': w_c_count, '西部农村': w_v_count}

def tuple2list91011(tuple: tuple, names: list):
    list = []
    for i in tuple:
        list.append({'value': i[1], 'name': i[0]})
    j = 0
    for i in names:
        flag = 0
        for k in list:
            for key, value in k.items():
                if value == i:
                    flag = 1
        if flag == 0:
            list.insert(j, {'value': 0, 'name': i})
        j += 1
    return list

def b_ns_count91011(table: str, col: str, username: str):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') group by " + col + ";"
    sql1 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区') group by " + col + ";"
    sql2 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区') group by " + col + ";"
    sql3 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省') group by " + col + ";"
    sql4 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省') group by " + col + ";"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = []
    for i in cursor.fetchall():
        total.append({'value': i[1], 'name': i[0]})  # 全部
    names = []
    for i in total:
        names.append(i["name"])
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_c_count = tuple2list91011(cursor.fetchall(), names)  # 北方城镇
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_v_count = tuple2list91011(cursor.fetchall(), names)  # 北方乡村
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_c_count = tuple2list91011(cursor.fetchall(), names)  # 南方城镇
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_v_count = tuple2list91011(cursor.fetchall(), names)  # 南方乡村
    return {'总体': total, '北方城镇': n_c_count, '北方农村': n_v_count, '南方城镇': s_c_count, '南方农村': s_v_count}

def b_ecw_count91011(table: str, col: str, username: str):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') group by " + col + ";"
    sql1 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省') group by " + col + ";"
    sql2 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省') group by " + col + ";"
    sql3 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省') group by " + col + ";"
    sql4 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省') group by " + col + ";"
    sql5 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区') group by " + col + ";"
    sql6 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区') group by " + col + ";"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = []
    for i in cursor.fetchall():
        total.append({'value': i[1], 'name': i[0]})  # 全部
    names = []
    for i in total:
        names.append(i["name"])  # 全部
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_c_count = tuple2list91011(cursor.fetchall(), names)  # 东部城镇
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_v_count = tuple2list91011(cursor.fetchall(), names)  # 东部乡村
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_c_count = tuple2list91011(cursor.fetchall(), names)  # 中部城镇
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_v_count = tuple2list91011(cursor.fetchall(), names)  # 中部乡村
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_c_count = tuple2list91011(cursor.fetchall(), names)  # 西部城镇
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_v_count = tuple2list91011(cursor.fetchall(), names)  # 西部乡村
    return {'总体': total, '东部城镇': e_c_count, '东部农村': e_v_count, '中部城镇': c_c_count, '中部农村': c_v_count, '西部城镇': w_c_count, '西部农村': w_v_count}


def count_quantiles16(tuple: tuple, quantiles: list):  # 根据四分位数统计个数
    first = second = third = fourth = 0
    for i in tuple:
        if float(i[0]) <= quantiles[0]:
            first += 1
        if (float(i[0]) > quantiles[0]) and (float(i[0]) <= quantiles[1]):
            second += 1
        if (float(i[0]) > quantiles[1]) and (float(i[0]) <= quantiles[2]):
            third += 1
        if float(i[0]) > quantiles[2]:
            fourth += 1
    tuple_list = [first, second, third, fourth]
    tuple_max = max(tuple_list)
    return {"names":['0—'+str(quantiles[0]), str(quantiles[0])+'—'+str(quantiles[1]), str(quantiles[1])+'—'+str(quantiles[2]), str(quantiles[2])+'—'+str(quantiles[3])],
            "max": tuple_max,
            "data": [{'value': first, 'name': '0—'+str(quantiles[0])},
                     {'value': second, 'name': str(quantiles[0])+'—'+str(quantiles[1])},
                     {'value': third, 'name': str(quantiles[1])+'—'+str(quantiles[2])},
                     {'value': fourth, 'name': str(quantiles[2])+'—'+str(quantiles[3])}]}

def a_ns_count16(table: str, col: str, username: str):
    db = pymysql.connect(host='82.156.173.187', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0');"
    sql1 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql2 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql3 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    sql4 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = cursor.fetchall()
    total2 = tuple2list91011a(total)  # 全部
    quantiles = np.percentile(total2, (25, 50, 75))
    quantiles = [float(quantiles[0]), float(quantiles[1]), float(quantiles[2])]
    quantiles.append(max(total2))
    total_count = count_quantiles16(total, quantiles)  # 总体四部分各有多少
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_c_all = cursor.fetchall()  # 北方城镇全部数据
    n_c_count = count_quantiles16(n_c_all, quantiles)  # 北方城镇四部分各有多少
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_v_all = cursor.fetchall()  # 北方乡村全部数据
    n_v_count = count_quantiles16(n_v_all, quantiles)  # 北方乡村四部分各有多少
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_c_all = cursor.fetchall()  # 南方城镇全部数据
    s_c_count = count_quantiles16(s_c_all, quantiles)  # 南方城镇四部分各有多少
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_v_all = cursor.fetchall()  # 南方乡村全部数据
    s_v_count = count_quantiles16(s_v_all, quantiles)  # 南方乡村四部分各有多少
    return {'总体': total_count, '北方城镇': n_c_count, '北方农村': n_v_count, '南方城镇': s_c_count, '南方农村': s_v_count}

def a_ecw_count16(table: str, col: str, username: str):
    db = pymysql.connect(host='82.156.173.187', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0');"
    sql1 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql2 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql3 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql4 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql5 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    sql6 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = cursor.fetchall()
    total2 = tuple2list91011a(total)  # 全部
    quantiles = np.percentile(total2, (25, 50, 75))
    quantiles = [float(quantiles[0]), float(quantiles[1]), float(quantiles[2])]
    quantiles.append(max(total2))
    total_count = count_quantiles16(total, quantiles)  # 总体四部分各有多少
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_c_all = cursor.fetchall()  # 东部城镇全部数据
    e_c_count = count_quantiles16(e_c_all, quantiles)  # 东部城镇四部分各有多少
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_v_all = cursor.fetchall()  # 东部乡村全部数据
    e_v_count = count_quantiles16(e_v_all, quantiles)  # 东部乡村四部分各有多少
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_c_all = cursor.fetchall()  # 中部城镇全部数据
    c_c_count = count_quantiles16(c_c_all, quantiles)  # 中部城镇四部分各有多少
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_v_all = cursor.fetchall()  # 中部乡村全部数据
    c_v_count = count_quantiles16(c_v_all, quantiles)  # 中部乡村四部分各有多少
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_c_all = cursor.fetchall()  # 西部城镇全部数据
    w_c_count = count_quantiles16(w_c_all, quantiles)  # 西部城镇四部分各有多少
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_v_all = cursor.fetchall()  # 西部乡村全部数据
    w_v_count = count_quantiles16(w_v_all, quantiles)  # 西部乡村四部分各有多少
    return {'总体': total_count, '东部城镇': e_c_count, '东部农村': e_v_count, '中部城镇': c_c_count, '中部农村': c_v_count, '西部城镇': w_c_count, '西部农村': w_v_count}

def tuple2list16(tuple: tuple, names: list):
    list = []
    tuple_list = []
    for i in tuple:
        tuple_list.append(i[1])
        list.append({'value': i[1], 'name': i[0]})
    tuple_max = max(tuple_list)
    j = 0
    for i in names:
        flag = 0
        for k in list:
            for key, value in k.items():
                if value == i:
                    flag = 1
        if flag == 0:
            list.insert(j, {'value': 0, 'name': i})
        j += 1
    return {"names": names, "max": tuple_max, "data": list}

def b_ns_count16(table: str, col: str, username: str):
    db = pymysql.connect(host='82.156.173.187', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') group by " + col + ";"
    sql1 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区') group by " + col + ";"
    sql2 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区') group by " + col + ";"
    sql3 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省') group by " + col + ";"
    sql4 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省') group by " + col + ";"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = []
    total_list = []
    for i in cursor.fetchall():
        total_list.append(i[1])
        total.append({'value': i[1], 'name': i[0]})  # 全部
    total_max = max(total_list)
    names = []
    for i in total:
        names.append(i["name"])
    total = {"names": names, "max": total_max, "data": total}
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_c_count = tuple2list16(cursor.fetchall(), names)  # 北方城镇
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_v_count = tuple2list16(cursor.fetchall(), names)  # 北方乡村
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_c_count = tuple2list16(cursor.fetchall(), names)  # 南方城镇
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_v_count = tuple2list16(cursor.fetchall(), names)  # 南方乡村
    return {'总体': total, '北方城镇': n_c_count, '北方农村': n_v_count, '南方城镇': s_c_count, '南方农村': s_v_count}

def b_ecw_count16(table: str, col: str, username: str):
    db = pymysql.connect(host='82.156.173.187', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') group by " + col + ";"
    sql1 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省') group by " + col + ";"
    sql2 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省') group by " + col + ";"
    sql3 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省') group by " + col + ";"
    sql4 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省') group by " + col + ";"
    sql5 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区') group by " + col + ";"
    sql6 = "SELECT " + col + ", COUNT(*) FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区') group by " + col + ";"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = []
    total_list = []
    for i in cursor.fetchall():
        total_list.append(i[1])
        total.append({'value': i[1], 'name': i[0]})  # 全部
    total_max = max(total_list)
    names = []
    for i in total:
        names.append(i["name"])  # 全部
    total = {"names": names, "max": total_max, "data": total}
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_c_count = tuple2list16(cursor.fetchall(), names)  # 东部城镇
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_v_count = tuple2list16(cursor.fetchall(), names)  # 东部乡村
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_c_count = tuple2list16(cursor.fetchall(), names)  # 中部城镇
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_v_count = tuple2list16(cursor.fetchall(), names)  # 中部乡村
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_c_count = tuple2list16(cursor.fetchall(), names)  # 西部城镇
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_v_count = tuple2list16(cursor.fetchall(), names)  # 西部乡村
    return {'总体': total, '东部城镇': e_c_count, '东部农村': e_v_count, '中部城镇': c_c_count, '中部农村': c_v_count, '西部城镇': w_c_count, '西部农村': w_v_count}



def tuple2list13140(tuple: tuple):
    list = []
    for i in tuple:
        list.append(float(i[1]))
    return list

def tuple2dict1314(tuple: tuple, min8: float, max8: float):
    dict = {}
    list = []
    for i in tuple:
        if (float(i[1]) > min8) and (float(i[1]) < max8):
            dict[i[0]] = i[1]
            list.append(float(i[1]))
    max0 = max(list)
    min0 = min(list)
    return [dict, max0, min0]

def couplelist(dict1: dict, dict2: dict):
    list = []
    for key, value in dict1.items():
        try:
            list.append([float(value), float(dict2[key])])
        except:
            pass
    return list

def aa_ns_count1314(table1: str, col1: str, table2: str, col2: str, username: str):
    if (table1[4:6] == '成人') or (table1[4:6] == '个人') or (table1[4:6] == '少儿'):
        id = 'pid'
    if table1[4:6] == '家庭':
        id = 'fid'
    if table1[4:6] == '村居':
        id = 'cid'
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table1[0:4] )
    cursor = db.cursor()
    sql0 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0');"
    sql1 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql2 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql3 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    sql4 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = cursor.fetchall()
    total2 = tuple2list13140(total)  # 全部
    quantiles = np.percentile(total2, (12.5, 25, 37.5, 50, 62.5, 75, 87.5))
    combine = tuple2dict1314(total, float(quantiles[0]), float(quantiles[6]))
    total1 = combine[0]  # 总体全部数据1
    total_x_max = combine[1]
    total_x_min = combine[2]
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    n_c_all1 = combine[0]  # 北方城镇全部数据1
    n_c_x_max = combine[1]
    n_c_x_min = combine[2]
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    n_v_all1 = combine[0]  # 北方乡村全部数据1
    n_v_x_max = combine[1]
    n_v_x_min = combine[2]
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    s_c_all1 = combine[0]  # 南方城镇全部数据1
    s_c_x_max = combine[1]
    s_c_x_min = combine[2]
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    s_v_all1 = combine[0]  # 南方乡村全部数据1
    s_v_x_max = combine[1]
    s_v_x_min = combine[2]
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table2[0:4] )
    cursor = db.cursor()
    sql0 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0');"
    sql1 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql2 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql3 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    sql4 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = cursor.fetchall()
    total2 = tuple2list13140(total)  # 全部
    quantiles = np.percentile(total2, (12.5, 25, 37.5, 50, 62.5, 75, 87.5))
    combine = tuple2dict1314(total, float(quantiles[0]), float(quantiles[6]))
    total2 = combine[0]  # 总体全部数据2
    total_y_max = combine[1]
    total_y_min = combine[2]
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    n_c_all2 = combine[0]  # 北方城镇全部数据2
    n_c_y_max = combine[1]
    n_c_y_min = combine[2]
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    n_v_all2 = combine[0]  # 北方乡村全部数据2
    n_v_y_max = combine[1]
    n_v_y_min = combine[2]
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    s_c_all2 = combine[0]  # 南方城镇全部数据2
    s_c_y_max = combine[1]
    s_c_y_min = combine[2]
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    s_v_all2 = combine[0]  # 南方乡村全部数据2
    s_v_y_max = combine[1]
    s_v_y_min = combine[2]
    total_couple = couplelist(total1, total2)
    n_c_couple = couplelist(n_c_all1, n_c_all2)
    n_v_couple = couplelist(n_v_all1, n_v_all2)
    s_c_couple = couplelist(s_c_all1, s_c_all2)
    s_v_couple = couplelist(s_v_all1, s_v_all2)
    return {'总体': total_couple, '总体m': [total_x_max, total_x_min, total_y_max, total_y_min], '北方城镇': n_c_couple, '北方城镇m': [n_c_x_max, n_c_x_min, n_c_y_max, n_c_y_min], '北方农村': n_v_couple, '北方农村m': [n_v_x_max, n_v_x_min, n_v_y_max, n_v_y_min], '南方城镇': s_c_couple, '南方城镇m': [s_c_x_max, s_c_x_min, s_c_y_max, s_c_y_min], '南方农村': s_v_couple, '南方农村m': [s_v_x_max, s_v_x_min, s_v_y_max, s_v_y_min]}

def aa_ecw_count1314(table1: str, col1: str, table2: str, col2: str, username: str):
    if (table1[4:6] == '成人') or (table1[4:6] == '个人') or (table1[4:6] == '少儿'):
        id = 'pid'
    if table1[4:6] == '家庭':
        id = 'fid'
    if table1[4:6] == '村居':
        id = 'cid'
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table1[0:4] )
    cursor = db.cursor()
    sql0 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0');"
    sql1 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql2 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql3 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql4 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql5 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    sql6 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = cursor.fetchall()
    total2 = tuple2list13140(total)  # 全部
    quantiles = np.percentile(total2, (12.5, 25, 37.5, 50, 62.5, 75, 87.5))
    combine = tuple2dict1314(total, float(quantiles[0]), float(quantiles[6]))
    total1 = combine[0]  # 总体全部数据1
    total_x_max = combine[1]
    total_x_min = combine[2]
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    e_c_all1 = combine[0]  # 东部城镇全部数据1
    e_c_x_max = combine[1]
    e_c_x_min = combine[2]
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    e_v_all1 = combine[0]  # 东部乡村全部数据1
    e_v_x_max = combine[1]
    e_v_x_min = combine[2]
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    c_c_all1 = combine[0]  # 中部城镇全部数据1
    c_c_x_max = combine[1]
    c_c_x_min = combine[2]
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    c_v_all1 = combine[0]  # 中部乡村全部数据1
    c_v_x_max = combine[1]
    c_v_x_min = combine[2]
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    w_c_all1 = combine[0]  # 西部城镇全部数据1
    w_c_x_max = combine[1]
    w_c_x_min = combine[2]
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    w_v_all1 = combine[0]  # 西部乡村全部数据1
    w_v_x_max = combine[1]
    w_v_x_min = combine[2]
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table2[0:4] )
    cursor = db.cursor()
    sql0 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0');"
    sql1 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql2 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql3 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql4 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql5 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    sql6 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    total = cursor.fetchall()
    total2 = tuple2list13140(total)  # 全部
    quantiles = np.percentile(total2, (12.5, 25, 37.5, 50, 62.5, 75, 87.5))
    combine = tuple2dict1314(total, float(quantiles[0]), float(quantiles[6]))
    total2 = combine[0]  # 总体全部数据2
    total_y_max = combine[1]
    total_y_min = combine[2]
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    e_c_all2 = combine[0]  # 东部城镇全部数据2
    e_c_y_max = combine[1]
    e_c_y_min = combine[2]
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    e_v_all2 = combine[0]  # 东部乡村全部数据2
    e_v_y_max = combine[1]
    e_v_y_min = combine[2]
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    c_c_all2 = combine[0]  # 中部城镇全部数据2
    c_c_y_max = combine[1]
    c_c_y_min = combine[2]
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    c_v_all2 = combine[0]  # 中部乡村全部数据2
    c_v_y_max = combine[1]
    c_v_y_min = combine[2]
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    w_c_all2 = combine[0]  # 西部城镇全部数据2
    w_c_y_max = combine[1]
    w_c_y_min = combine[2]
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    combine = tuple2dict1314(cursor.fetchall(), float(quantiles[0]), float(quantiles[6]))
    w_v_all2 = combine[0]  # 西部乡村全部数据1
    w_v_y_max = combine[1]
    w_v_y_min = combine[2]
    total_couple = couplelist(total1, total2)
    e_c_couple = couplelist(e_c_all1, e_c_all2)
    e_v_couple = couplelist(e_v_all1, e_v_all2)
    c_c_couple = couplelist(c_c_all1, c_c_all2)
    c_v_couple = couplelist(c_v_all1, c_v_all2)
    w_c_couple = couplelist(w_c_all1, w_c_all2)
    w_v_couple = couplelist(w_v_all1, w_v_all2)
    return {'总体': total_couple, '总体m': [total_x_max, total_x_min, total_y_max, total_y_min], '东部城镇': e_c_couple, '东部城镇m': [e_c_x_max, e_c_x_min, e_c_y_max, e_c_y_min], '东部农村': e_v_couple, '东部农村m': [e_v_x_max, e_v_x_min, e_v_y_max, e_v_y_min], '中部城镇': c_c_couple, '中部城镇m': [c_c_x_max, c_c_x_min, c_c_y_max, c_c_y_min], '中部农村': c_v_couple, '中部农村m': [c_v_x_max, c_v_x_min, c_v_y_max, c_v_y_min], '西部城镇': w_c_couple, '西部城镇m': [w_c_x_max, w_c_x_min, w_c_y_max, w_c_y_min], '西部农村': w_v_couple, '西部农村m': [w_v_x_max, w_v_x_min, w_v_y_max, w_v_y_min]}



def couple3list(dict1: dict, dict2: dict, dict3: dict, area: str):
    list = []
    for key, value in dict1.items():
        try:
            list.append([float(value), float(dict2[key]), float(dict3[key])*10000, area])
        except:
            pass
    return list

def aaa_ns_count15(table1: str, col1: str, table2: str, col2: str, table3: str, col3: str, username: str):
    if (table1[4:6] == '成人') or (table1[4:6] == '个人') or (table1[4:6] == '少儿'):
        id = 'pid'
    if table1[4:6] == '家庭':
        id = 'fid'
    if table1[4:6] == '村居':
        id = 'cid'
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table1[0:4] )
    cursor = db.cursor()
    sql1 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql2 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql3 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    sql4 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_c_all1 = tuple2dict1314(cursor.fetchall())[0]  # 北方城镇全部数据1
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_v_all1 = tuple2dict1314(cursor.fetchall())[0]  # 北方乡村全部数据1
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_c_all1 = tuple2dict1314(cursor.fetchall())[0]  # 南方城镇全部数据1
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_v_all1 = tuple2dict1314(cursor.fetchall())[0]  # 南方乡村全部数据1
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table2[0:4] )
    cursor = db.cursor()
    sql1 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql2 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql3 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    sql4 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_c_all2 = tuple2dict1314(cursor.fetchall())[0]  # 北方城镇全部数据2
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_v_all2 = tuple2dict1314(cursor.fetchall())[0]  # 北方乡村全部数据2
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_c_all2 = tuple2dict1314(cursor.fetchall())[0]  # 南方城镇全部数据2
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_v_all2 = tuple2dict1314(cursor.fetchall())[0]  # 南方乡村全部数据2
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table3[0:4] )
    cursor = db.cursor()
    sql1 = "SELECT " + id + ', ' + col3 + " FROM " + table3 + "_" + username + " WHERE (" + col3 + " != '不适用' and " + col3 + " != '不知道' and " + col3 + " != '拒绝回答' and " + col3 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql2 = "SELECT " + id + ', ' + col3 + " FROM " + table3 + "_" + username + " WHERE (" + col3 + " != '不适用' and " + col3 + " != '不知道' and " + col3 + " != '拒绝回答' and " + col3 + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql3 = "SELECT " + id + ', ' + col3 + " FROM " + table3 + "_" + username + " WHERE (" + col3 + " != '不适用' and " + col3 + " != '不知道' and " + col3 + " != '拒绝回答' and " + col3 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    sql4 = "SELECT " + id + ', ' + col3 + " FROM " + table3 + "_" + username + " WHERE (" + col3 + " != '不适用' and " + col3 + " != '不知道' and " + col3 + " != '拒绝回答' and " + col3 + " != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_c_all3 = tuple2dict1314(cursor.fetchall())[0]  # 北方城镇全部数据3
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    n_v_all3 = tuple2dict1314(cursor.fetchall())[0]  # 北方乡村全部数据3
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_c_all3 = tuple2dict1314(cursor.fetchall())[0]  # 南方城镇全部数据3
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    s_v_all3 = tuple2dict1314(cursor.fetchall())[0]  # 南方乡村全部数据3
    n_c_couple = couple3list(n_c_all1, n_c_all2, n_c_all3, '北方城镇')
    n_v_couple = couple3list(n_v_all1, n_v_all2, n_v_all3, '北方农村')
    s_c_couple = couple3list(s_c_all1, s_c_all2, s_c_all3, '南方城镇')
    s_v_couple = couple3list(s_v_all1, s_v_all2, s_v_all3, '南方农村')
    return {"header": ["北方城镇", "北方农村", "南方城镇", "南方农村"], "data": [n_c_couple, n_v_couple, s_c_couple, s_v_couple]}

def aaa_ecw_count15(table1: str, col1: str, table2: str, col2: str, table3: str, col3: str, username: str):
    if (table1[4:6] == '成人') or (table1[4:6] == '个人') or (table1[4:6] == '少儿'):
        id = 'pid'
    if table1[4:6] == '家庭':
        id = 'fid'
    if table1[4:6] == '村居':
        id = 'cid'
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table1[0:4] )
    cursor = db.cursor()
    sql1 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql2 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql3 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql4 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql5 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    sql6 = "SELECT " + id + ', ' + col1 + " FROM " + table1 + "_" + username + " WHERE (" + col1 + " != '不适用' and " + col1 + " != '不知道' and " + col1 + " != '拒绝回答' and " + col1 + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_c_all1 = tuple2dict1314(cursor.fetchall())[0]  # 东部城镇全部数据1
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_v_all1 = tuple2dict1314(cursor.fetchall())[0]  # 东部乡村全部数据1
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_c_all1 = tuple2dict1314(cursor.fetchall())[0]  # 中部城镇全部数据1
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_v_all1 = tuple2dict1314(cursor.fetchall())[0]  # 中部乡村全部数据1
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_c_all1 = tuple2dict1314(cursor.fetchall())[0]  # 西部城镇全部数据1
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_v_all1 = tuple2dict1314(cursor.fetchall())[0]  # 西部乡村全部数据1
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table2[0:4] )
    cursor = db.cursor()
    sql1 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql2 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql3 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql4 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql5 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    sql6 = "SELECT " + id + ', ' + col2 + " FROM " + table2 + "_" + username + " WHERE (" + col2 + " != '不适用' and " + col2 + " != '不知道' and " + col2 + " != '拒绝回答' and " + col2 + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_c_all2 = tuple2dict1314(cursor.fetchall())[0]  # 东部城镇全部数据2
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_v_all2 = tuple2dict1314(cursor.fetchall())[0]  # 东部乡村全部数据2
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_c_all2 = tuple2dict1314(cursor.fetchall())[0]  # 中部城镇全部数据2
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_v_all2 = tuple2dict1314(cursor.fetchall())[0]  # 中部乡村全部数据2
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_c_all2 = tuple2dict1314(cursor.fetchall())[0]  # 西部城镇全部数据2
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_v_all2 = tuple2dict1314(cursor.fetchall())[0]  # 西部乡村全部数据2
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table3[0:4] )
    cursor = db.cursor()
    sql1 = "SELECT " + id + ', ' + col3 + " FROM " + table3 + "_" + username + " WHERE (" + col3 + " != '不适用' and " + col3 + " != '不知道' and " + col3 + " != '拒绝回答' and " + col3 + " != '0') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql2 = "SELECT " + id + ', ' + col3 + " FROM " + table3 + "_" + username + " WHERE (" + col3 + " != '不适用' and " + col3 + " != '不知道' and " + col3 + " != '拒绝回答' and " + col3 + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql3 = "SELECT " + id + ', ' + col3 + " FROM " + table3 + "_" + username + " WHERE (" + col3 + " != '不适用' and " + col3 + " != '不知道' and " + col3 + " != '拒绝回答' and " + col3 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql4 = "SELECT " + id + ', ' + col3 + " FROM " + table3 + "_" + username + " WHERE (" + col3 + " != '不适用' and " + col3 + " != '不知道' and " + col3 + " != '拒绝回答' and " + col3 + " != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql5 = "SELECT " + id + ', ' + col3 + " FROM " + table3 + "_" + username + " WHERE (" + col3 + " != '不适用' and " + col3 + " != '不知道' and " + col3 + " != '拒绝回答' and " + col3 + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    sql6 = "SELECT " + id + ', ' + col3 + " FROM " + table3 + "_" + username + " WHERE (" + col3 + " != '不适用' and " + col3 + " != '不知道' and " + col3 + " != '拒绝回答' and " + col3 + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_c_all3 = tuple2dict1314(cursor.fetchall())[0]  # 东部城镇全部数据3
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    e_v_all3 = tuple2dict1314(cursor.fetchall())[0]  # 东部乡村全部数据3
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_c_all3 = tuple2dict1314(cursor.fetchall())[0]  # 中部城镇全部数据3
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    c_v_all3 = tuple2dict1314(cursor.fetchall())[0]  # 中部乡村全部数据3
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_c_all3 = tuple2dict1314(cursor.fetchall())[0]  # 西部城镇全部数据3
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误"}
    w_v_all3 = tuple2dict1314(cursor.fetchall())[0]  # 西部乡村全部数据3
    e_c_couple = couple3list(e_c_all1, e_c_all2, e_c_all3, '东部城镇')
    e_v_couple = couple3list(e_v_all1, e_v_all2, e_v_all3, '东部农村')
    c_c_couple = couple3list(c_c_all1, c_c_all2, c_c_all3, '中部城镇')
    c_v_couple = couple3list(c_v_all1, c_v_all2, c_v_all3, '中部农村')
    w_c_couple = couple3list(w_c_all1, w_c_all2, w_c_all3, '西部城镇')
    w_v_couple = couple3list(w_v_all1, w_v_all2, w_v_all3, '西部农村')
    return {"header": ["东部城镇", "东部农村", "中部城镇", "中部农村", "西部城镇", "西部农村"], "data": [e_c_couple, e_v_couple, c_c_couple, c_v_couple, w_c_couple, w_v_couple]}



def tuple2list(tuple: tuple):
    list = []
    for i in tuple:
        list.append(i[0])
    return list

def a_ns_count17(table: str, col: str, username: str):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0');"
    sql1 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql2 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '河南省' or provcd = '山西省' or provcd = '陕西省' or provcd = '甘肃省' or provcd = '青海省' or provcd = '新疆维吾尔自治区' or provcd = '河北省' or provcd = '天津市' or provcd = '北京市' or provcd = '内蒙古自治区' or provcd = '辽宁省' or provcd = '吉林省' or provcd = '黑龙江省' or provcd = '宁夏回族自治区');"
    sql3 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    sql4 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '江苏省' or provcd = '浙江省' or provcd = '福建省' or provcd = '广东省' or provcd = '江西省' or provcd = '湖北省' or provcd = '广西壮族自治区' or provcd = '湖南省' or provcd = '上海市' or provcd = '重庆市' or provcd = '西藏自治区' or provcd = '贵州省' or provcd = '四川省' or provcd = '云南省' or provcd = '安徽省');"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql0}
    total = tuple2list(cursor.fetchall())
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql1}
    n_c_all = tuple2list(cursor.fetchall())  # 北方城镇全部数据
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql2}
    n_v_all = tuple2list(cursor.fetchall())  # 北方乡村全部数据
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql3}
    s_c_all = tuple2list(cursor.fetchall())  # 南方城镇全部数据
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql4}
    s_v_all = tuple2list(cursor.fetchall())  # 南方乡村全部数据
    return [total, n_c_all, n_v_all, s_c_all, s_v_all]

def a_ecw_count17(table: str, col: str, username: str):
    db = pymysql.connect(host='localhost', user='root', password='zyy917382', database="cfps" + table[0:4])
    cursor = db.cursor()
    sql0 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0');"
    sql1 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql2 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山东省' or provcd = '浙江省' or provcd = '江苏省' or provcd = '福建省' or provcd = '广东省' or provcd = '北京市' or provcd = '天津市' or provcd = '河北省' or provcd = '上海市' or provcd = '辽宁省' or provcd = '海南省');"
    sql3 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql4 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '山西省' or provcd = '河南省' or provcd = '安徽省' or provcd = '湖北省' or provcd = '江西省' or provcd = '湖南省' or provcd = '黑龙江省' or provcd = '吉林省');"
    sql5 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '城镇' or urban = '城市') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    sql6 = "SELECT " + col + " FROM " + table + "_" + username + " WHERE (" + col + " != '不适用' and " + col + " != '不知道' and " + col + " != '拒绝回答' and " + col + " != '0') and (urban = '乡村') and (provcd = '青海省' or provcd = '甘肃省' or provcd = '四川省' or provcd = '贵州省' or provcd = '云南省' or provcd = '陕西省' or provcd = '内蒙古自治区' or provcd = '西藏自治区' or provcd = '广西壮族自治区' or provcd = '宁夏回族自治区' or provcd = '重庆市' or provcd = '新疆维吾尔自治区');"
    try:
        cursor.execute(sql0)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql0}
    total = tuple2list(cursor.fetchall())
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql1}
    e_c_all = tuple2list(cursor.fetchall())  # 东部城镇全部数据
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql2}
    e_v_all = tuple2list(cursor.fetchall())  # 东部乡村全部数据
    try:
        cursor.execute(sql3)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql3}
    c_c_all = tuple2list(cursor.fetchall())  # 中部城镇全部数据
    try:
        cursor.execute(sql4)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql4}
    c_v_all = tuple2list(cursor.fetchall())  # 中部乡村全部数据
    try:
        cursor.execute(sql5)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql5}
    w_c_all = tuple2list(cursor.fetchall())  # 西部城镇全部数据
    try:
        cursor.execute(sql6)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return {"status": "failure", "reason": "内部错误", "sql": sql6}
    w_v_all = tuple2list(cursor.fetchall())  # 西部乡村全部数据
    return [total, e_c_all, e_v_all, c_c_all, c_v_all, w_c_all, w_v_all]



def nab_nsecw_count192021(mes: list):
    num = 0
    username = mes[3]
    if mes[0] == 'ns':
        res = {"header": ["北方城镇", "北方农村", "南方城镇", "南方农村"]}
        for key, value in (mes[1]).items():
            if value[1] == 'a':
                res0 = a_ns_count91011(key, value[0], username)
            if value[1] == 'b':
                res0 = b_ns_count91011(key, value[0], username)
            k = 0
            for i in res0["总体"]:
                res[letters[num]+str(k)] = {"name": i["name"], "data": [res0["北方城镇"][k]["value"], res0["北方农村"][k]["value"], res0["南方城镇"][k]["value"], res0["南方农村"][k]["value"]]}
                k += 1
            flag = 0
            while flag == 0:
                if k < 8:
                    res[letters[num] + str(k)] = {"name": "", "data": []}
                    k += 1
                else:
                    flag = 1
            num += 1
        while num < 3:
            k = 0
            for i in res0["总体"]:
                res[letters[num]+str(k)] = {"name": "", "data": []}
                k += 1
            flag = 0
            while flag == 0:
                if k < 8:
                    res[letters[num] + str(k)] = {"name": "", "data": []}
                    k += 1
                else:
                    flag = 1
            num += 1
        return res
    if mes[0] == 'ecw':
        res = {"header": ["东部城镇", "东部农村", "中部城镇", "中部农村", "西部城镇", "西部农村"]}
        for key, value in (mes[1]).items():
            if value[1] == 'a':
                res0 = a_ecw_count91011(key, value[0], username)
            if value[1] == 'b':
                res0 = b_ecw_count91011(key, value[0], username)
            k = 0
            for i in res0["总体"]:
                res[letters[num] + str(k)] = {"name": i["name"], "data": [res0["东部城镇"][k]["value"], res0["东部农村"][k]["value"], res0["中部城镇"][k]["value"], res0["中部农村"][k]["value"], res0["西部城镇"][k]["value"], res0["西部农村"][k]["value"]]}
                k += 1
            flag = 0
            while flag == 0:
                if k < 8:
                    res[letters[num] + str(k)] = {"name": "", "data": []}
                    k += 1
                else:
                    flag = 1
            num += 1
        while num < 3:
            k = 0
            for i in res0["总体"]:
                res[letters[num]+str(k)] = {"name": "", "data": []}
                k += 1
            flag = 0
            while flag == 0:
                if k < 8:
                    res[letters[num] + str(k)] = {"name": "", "data": []}
                    k += 1
                else:
                    flag = 1
            num += 1
        return res

def percentage(res: dict, sum: float, area: str):  #将数值换为百分比
    k = 0
    if sum != 0:
        for i in res[area]:
            res[area][k]["value"] = round(i["value"]/sum, 3)
            k += 1
    else:
        for i in res[area]:
            res[area][k]["value"] = 0
            k += 1
    return res

def nab_nsecw_count22(mes: list):
    num = 0
    username = mes[2]
    if mes[0] == 'ns':
        res = {"header": ["总体", "北方城镇", "北方农村", "南方城镇", "南方农村"]}
        for key, value in (mes[1]).items():
            if value[1] == 'a':
                res0 = a_ns_count91011(key, value[0], username)
            if value[1] == 'b':
                res0 = b_ns_count91011(key, value[0], username)
            sum0 = float(0)
            sum1 = float(0)
            sum2 = float(0)
            sum3 = float(0)
            sum4 = float(0)
            for i in res0["总体"]:
                sum0 += i["value"]
            for i in res0["北方城镇"]:
                sum1 += i["value"]
            for i in res0["北方农村"]:
                sum2 += i["value"]
            for i in res0["南方城镇"]:
                sum3 += i["value"]
            for i in res0["南方农村"]:
                sum4 += i["value"]
            res1 = percentage(res0, sum0, "总体")
            res1 = percentage(res1, sum1, "北方城镇")
            res1 = percentage(res1, sum2, "北方农村")
            res1 = percentage(res1, sum3, "南方城镇")
            res1 = percentage(res1, sum4, "南方农村")
            k = 0
            for i in res1["总体"]:
                res[letters[num]+str(k)] = {"name": i["name"], "data": [i["value"], res1["北方城镇"][k]["value"], res1["北方农村"][k]["value"], res1["南方城镇"][k]["value"], res1["南方农村"][k]["value"]]}
                k += 1
            flag = 0
            while flag == 0:
                if k < 8:
                    res[letters[num] + str(k)] = {"name": "", "data": []}
                    k += 1
                else:
                    flag = 1
            num += 1
        while num < 3:
            k = 0
            for i in res0["总体"]:
                res[letters[num] + str(k)] = {"name": "", "data": []}
                k += 1
            flag = 0
            while flag == 0:
                if k < 8:
                    res[letters[num] + str(k)] = {"name": "", "data": []}
                    k += 1
                else:
                    flag = 1
            num += 1
        return res
    if mes[0] == 'ecw':
        res = {"header": ["总体", "东部城镇", "东部农村", "中部城镇", "中部农村", "西部城镇", "西部农村"]}
        for key, value in (mes[1]).items():
            if value[1] == 'a':
                res0 = a_ecw_count91011(key, value[0], username)
            if value[1] == 'b':
                res0 = b_ecw_count91011(key, value[0], username)
            sum0 = float(0)
            sum1 = float(0)
            sum2 = float(0)
            sum3 = float(0)
            sum4 = float(0)
            sum5 = float(0)
            sum6 = float(0)
            for i in res0["总体"]:
                sum0 += i["value"]
            for i in res0["东部城镇"]:
                sum1 += i["value"]
            for i in res0["东部农村"]:
                sum2 += i["value"]
            for i in res0["中部城镇"]:
                sum3 += i["value"]
            for i in res0["中部农村"]:
                sum4 += i["value"]
            for i in res0["西部城镇"]:
                sum5 += i["value"]
            for i in res0["西部农村"]:
                sum6 += i["value"]
            res1 = percentage(res0, sum0, "总体")
            res1 = percentage(res1, sum1, "东部城镇")
            res1 = percentage(res1, sum2, "东部农村")
            res1 = percentage(res1, sum3, "中部城镇")
            res1 = percentage(res1, sum4, "中部农村")
            res1 = percentage(res1, sum5, "西部城镇")
            res1 = percentage(res1, sum6, "西部农村")
            k = 0
            for i in res1["总体"]:
                res[letters[num] + str(k)] = {"name": i["name"], "data": [i["value"], res1["东部城镇"][k]["value"], res1["东部农村"][k]["value"], res1["中部城镇"][k]["value"], res1["中部农村"][k]["value"], res1["西部城镇"][k]["value"], res1["西部农村"][k]["value"]]}
                k += 1
            flag = 0
            while flag == 0:
                if k < 8:
                    res[letters[num] + str(k)] = {"name": "", "data": []}
                    k += 1
                else:
                    flag = 1
            num += 1
        while num < 3:
            k = 0
            for i in res0["总体"]:
                res[letters[num] + str(k)] = {"name": "", "data": []}
                k += 1
            flag = 0
            while flag == 0:
                if k < 8:
                    res[letters[num] + str(k)] = {"name": "", "data": []}
                    k += 1
                else:
                    flag = 1
            num += 1
        return res



def b_ns_count23(table: str, col: str, username: str):
    res0 = b_ns_count8(table, col, username)
    yheader = ["北方城镇", "北方农村", "南方城镇", "南方农村"]
    xheader = []
    data = []
    i = 0  # x轴参数，即回答的答案
    for key, value in res0.items():
        if key != "header":
            xheader.append(value["name"])
            j = 0  # y轴参数，即地区
            for k in value["data"]:
                data.append([i, j, k])
                j += 1
            i += 1
    return {"xheader": xheader, "yheader": yheader, "data": data}

def b_ecw_count23(table: str, col: str, username: str):
    res0 = b_ecw_count8(table, col, username)
    yheader = ["东部城镇", "东部农村", "中部城镇", "中部农村", "西部城镇", "西部农村"]
    xheader = []
    data = []
    i = 0  # x轴参数，即回答的答案
    for key, value in res0.items():
        if key != "header":
            xheader.append(value["name"])
            j = 0  # y轴参数，即地区
            for k in value["data"]:
                data.append([i, j, k])
                j += 1
            i += 1
    return {"xheader": xheader, "yheader": yheader, "data": data}
