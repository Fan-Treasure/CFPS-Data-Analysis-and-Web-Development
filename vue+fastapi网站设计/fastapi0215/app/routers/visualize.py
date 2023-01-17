from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from app.models.visualize import count
from utils.visualize import *
import json

router = APIRouter()

@router.post('/count')
async def Count(request: count, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    username = Authorize.get_jwt_subject()
    tip = request.tip
    tubiao = request.tubiao
    region = request.region
    table1 = tip["tubiao1"]
    table2 = tip["tubiao2"]
    table3 = tip["tubiao3"]
    col1_cn = tip["biaoqian1"]
    col2_cn = tip["biaoqian2"]
    col3_cn = tip["biaoqian3"]
    type1 = tip["type1"]
    type2 = tip["type2"]
    type3 = tip["type3"]
    with open("data/"+username+"/col_names.json", encoding="utf-8") as f:
        col_names = json.load(f)
    if tubiao == '1' or tubiao == '2' or tubiao == '3' or tubiao == '4' or tubiao == '5' or tubiao == '25':  # 基础折线图、面积图、柱状图、极坐标柱状图、条形图、象形柱状图
        if table1 != '1' and table2 == '1' and table3 == '1':  # 只选了一列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            if type1 == 'a' and region == '1':  # 南北；计算平均值型
                return a_ns_count12345(table1, col1_eng, tubiao, username)
            if type1 == 'a' and region == '2':  # 东中西；计算平均值型
                return a_ecw_count12345(table1, col1_eng, tubiao, username)
            else:
                return {"status": "failure", "reason": "若绘制折线图/面积图/柱状图/极坐标柱状图/条形图/象形柱状图，请选择一列可计算数值型的数据，如“个人收入”"}
        else:
            return {"status": "failure", "reason": "若绘制折线图/面积图/柱状图/极坐标柱状图/条形图，请选择一列可计算数值型的数据，如“个人收入”"}
    if tubiao == '6' or tubiao == '7':  # 堆叠折线图、堆叠面积图
        if table1 != '1' and table2 != '1' and table3 == '1':  # 选了两列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            if type1 == 'a' and type2 == 'a' and region == '1':  # 南北；两个均为计算平均值型
                return {"header": ["北方城镇", "北方农村", "南方城镇", "南方农村"], "a0": {"name": col1_cn, "data":a_ns_count12345(table1, col1_eng, '1', username)["data"]}, "a1": {"name": col2_cn, "data":a_ns_count12345(table2, col2_eng, '1', username)["data"]}}
            if type1 == 'a' and type2 == 'a' and region == '2':  # 东中西；两个均为计算平均值型
                return {"header": ["东部城镇", "东部农村", "中部城镇", "中部农村", "西部城镇", "西部农村"], "a0": {"name": col1_cn, "data":a_ecw_count12345(table1, col1_eng, '1', username)["data"]}, "a1": {"name": col2_cn, "data":a_ecw_count12345(table2, col2_eng, '1', username)["data"]}}
            else:
                return {"status": "failure", "reason": "若绘制堆叠折线图/堆叠面积图，请选择两列或两列以上可计算数值型的数据，如“个人收入”，且必须是同一问题的多年对比"}
        if table1 != '1' and table2 != '1' and table3 != '1':  # 选了三列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            col3_eng = col_names[table3[0:4]][table3][col3_cn][1]
            if type1 == 'a' and type2 == 'a' and type3 == 'a' and region == '1':  # 南北；三个均为计算平均值型
                return {"header": ["北方城镇", "北方农村", "南方城镇", "南方农村"], "a0": {"name": col1_cn, "data":a_ns_count12345(table1, col1_eng, '1', username)["data"]}, "a1": {"name": col2_cn, "data":a_ns_count12345(table2, col2_eng, '1', username)["data"]}, "a2": {"name": col3_cn, "data":a_ns_count12345(table3, col3_eng, '1', username)["data"]}}
            if type1 == 'a' and type2 == 'a' and type3 == 'a' and region == '2':  # 东中西；三个均为计算平均值型
                return {"header": ["东部城镇", "东部农村", "中部城镇", "中部农村", "西部城镇", "西部农村"], "a0": {"name": col1_cn, "data":a_ecw_count12345(table1, col1_eng, '1', username)["data"]}, "a1": {"name": col2_cn, "data":a_ecw_count12345(table2, col2_eng, '1', username)["data"]}, "a2": {"name": col3_cn, "data":a_ecw_count12345(table3, col3_eng, '1', username)["data"]}}
            else:
                return {"status": "failure", "reason": "若绘制堆叠折线图/堆叠面积图，请选择两列或两列以上可计算数值型的数据，如“个人收入”，且必须是同一问题的多年对比"}
        else:
            return {"status": "failure", "reason": "若绘制堆叠折线图/堆叠面积图，请选择两列或两列以上可计算数值型的数据，如“个人收入”，且必须是同一问题的多年对比"}
    if tubiao == '8':  # 堆叠柱状图
        if table1 != '1' and table2 == '1' and table3 == '1':  # 只选了一列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            if type1 == 'b' and region == '1':  # 南北；计算比例型
                return b_ns_count8(table1, col1_eng, username)
            if type1 == 'b' and region == '2':  # 东中西；计算比例型
                return b_ecw_count8(table1, col1_eng, username)
            else:
                return {"status": "failure", "reason": "若绘制堆叠柱状图，请选择一列可计算比例型的数据，如“您家做饭用的水最主要是”"}
        else:
            return {"status": "failure", "reason": "若绘制堆叠柱状图，请选择一列可计算比例型的数据，如“您家做饭用的水最主要是”"}
    if tubiao == '9' or tubiao == '10' or tubiao == '11':  # 饼图、环形图、玫瑰图
        if table1 != '1' and table2 == '1' and table3 == '1':  # 只选了一列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            if type1 == 'a' and region == '1':  # 南北；计算数值型
                return a_ns_count91011(table1, col1_eng, username)
            if type1 == 'a' and region == '2':  # 东中西；计算数值型
                return a_ecw_count91011(table1, col1_eng, username)
            if type1 == 'b' and region == '1':  # 南北；计算比例型
                return b_ns_count91011(table1, col1_eng, username)
            if type1 == 'b' and region == '2':  # 东中西；计算比例型
                return b_ecw_count91011(table1, col1_eng, username)
            else:
                return {"status": "failure", "reason": "若绘制饼图/环形图/玫瑰图，请选择一列数据"}
        else:
            return {"status": "failure", "reason": "若绘制饼图/环形图/玫瑰图，请选择一列数据"}
    if tubiao == '12':  # 嵌套环形图
        if table1 != '1' and table2 != '1' and table3 == '1':  # 选了两列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            if type1 == 'a' and type2 == 'a' and region == '1':  # 南北；两个都为均值型
                return {"data1": a_ns_count91011(table1, col1_eng, username), "data2": a_ns_count91011(table2, col2_eng, username)}
            if type1 == 'a' and type2 == 'a' and region == '2':  # 东中西；两个都为均值型
                return {"data1": a_ecw_count91011(table1, col1_eng, username), "data2": a_ecw_count91011(table2, col2_eng, username)}
            if type1 == 'a' and type2 == 'b' and region == '1':  # 南北；第一个为均值型，第二个为比例型
                return {"data1": a_ns_count91011(table1, col1_eng, username), "data2": b_ns_count91011(table2, col2_eng, username)}
            if type1 == 'a' and type2 == 'b' and region == '2':  # 东中西；第一个为均值型，第二个为比例型
                return {"data1": a_ecw_count91011(table1, col1_eng, username), "data2": b_ecw_count91011(table2, col2_eng, username)}
            if type1 == 'b' and type2 == 'a' and region == '1':  # 南北；第一个为比例型，第二个为均值型
                return {"data1": b_ns_count91011(table1, col1_eng, username), "data2": a_ns_count91011(table2, col2_eng, username)}
            if type1 == 'b' and type2 == 'a' and region == '2':  # 东中西；第一个为比例型，第二个为均值型
                return {"data1": b_ecw_count91011(table1, col1_eng, username), "data2": a_ecw_count91011(table2, col2_eng, username)}
            if type1 == 'b' and type2 == 'b' and region == '1':  # 南北；两个都为比例型
                return {"data1": b_ns_count91011(table1, col1_eng, username), "data2": b_ns_count91011(table2, col2_eng, username)}
            if type1 == 'b' and type2 == 'b' and region == '2':  # 东中西；两个都为比例型
                return {"data1": b_ecw_count91011(table1, col1_eng, username), "data2": b_ecw_count91011(table2, col2_eng, username)}
        else:
            return {"status": "failure", "reason": "若绘制嵌套环形图，请选择两列数据"}
    if tubiao == '13' or tubiao == '14':  # 基础散点图、线性回归图
        if table1 != '1' and table2 != '1' and table3 == '1' and table1[4:6] == table2[4:6]:  # 选了两列数据，而且属于同一大类
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            if type1 == 'a' and type2 == 'a' and region == '1':  # 南北；两个都为均值型
                return aa_ns_count1314(table1, col1_eng, table2, col2_eng, username)
            if type1 == 'a' and type2 == 'a' and region == '2':  # 东中西；两个都为均值型
                return aa_ecw_count1314(table1, col1_eng, table2, col2_eng, username)
            else:
                return {"status": "failure", "reason": "若绘制基础散点图/线性回归图，请选择同一大类（成人 少儿 家庭 村居）的两列数据，如从2010成人A基本信息和2012成人C教育中各取一列"}
        else:
            return {"status": "failure", "reason": "若绘制基础散点图/线性回归图，请选择同一大类（成人 少儿 家庭 村居）的两列数据，如从2010成人A基本信息和2012成人C教育中各取一列"}
    if tubiao == '15':  # 气泡图
        if table1 != '1' and table2 != '1' and table3 != '1' and table1[4:6] == table2[4:6] == table2[4:6]:  # 选了三列数据，而且属于同一大类
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            col3_eng = col_names[table3[0:4]][table3][col3_cn][1]
            if type1 == 'a' and type2 == 'a' and type3 == 'a' and region == '1':  # 南北；三个都为均值型
                return aaa_ns_count15(table1, col1_eng, table2, col2_eng, table3, col3_eng, username)
            if type1 == 'a' and type2 == 'a' and type3 == 'a' and region == '2':  # 东中西；三个都为均值型
                return aaa_ecw_count15(table1, col1_eng, table2, col2_eng, table3, col3_eng, username)
            else:
                return {"status": "failure", "reason": "若绘制气泡图，请选择同一大类（成人 少儿 家庭 村居）的三列数据，如从2010成人A基本信息、2012成人C教育、2012成人G工作中各取一列"}
        else:
            return {"status": "failure", "reason": "若绘制气泡图，请选择同一大类（成人 少儿 家庭 村居）的三列数据，如从2010成人A基本信息、2012成人C教育、2012成人G工作中各取一列"}
    if tubiao == '16':  # 漏斗图
        if table1 != '1' and table2 == '1' and table3 == '1':  # 只选了一列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            if type1 == 'a' and region == '1':  # 南北；计算数值型
                return a_ns_count16(table1, col1_eng, username)
            if type1 == 'a' and region == '2':  # 东中西；计算数值型
                return a_ecw_count16(table1, col1_eng, username)
            if type1 == 'b' and region == '1':  # 南北；计算比例型
                return b_ns_count16(table1, col1_eng, username)
            if type1 == 'b' and region == '2':  # 东中西；计算比例型
                return b_ecw_count16(table1, col1_eng, username)
            else:
                return {"status": "failure", "reason": "若绘漏斗图，请选择一列数据"}
        else:
            return {"status": "failure", "reason": "若绘漏斗图，请选择一列数据"}
    if tubiao == '17':  # 基础盒须图
        if table1 != '1' and table2 == '1' and table3 == '1':  # 只选了一列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            if type1 == 'a' and region == '1':  # 南北；计算数值型
                res = a_ns_count17(table1, col1_eng, username)
                return {"header": ["总体", "北方城镇", "北方农村", "南方城镇", "南方农村"], "data": res}
            if type1 == 'a' and region == '2':  # 东中西；计算数值型
                res = a_ecw_count17(table1, col1_eng, username)
                return {"header": ["总体", "东部城镇", "东部农村", "中部城镇", "中部农村", "西部城镇", "西部农村"], "data": res}
            else:
                return {"status": "failure", "reason": "若绘制盒须图，请选择一列可计算数值型的数据，如“个人收入”"}
        else:
            return {"status": "failure", "reason": "若绘制盒须图，请选择一列可计算数值型的数据，如“个人收入”"}
    if tubiao == '18':  # 多系列盒须图
        if table1 != '1' and table2 != '1' and table3 == '1':  # 选了两列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            if type1 == 'a' and type2 == 'a' and region == '1':  # 南北；两个均为计算平均值型
                pass
            if type1 == 'a' and type2 == 'a' and region == '2':  # 东中西；两个均为计算平均值型
                pass
            else:
                return {"status": "failure", "reason": "若绘制多系列盒须图，请选择两列或两列以上可计算数值型的数据，如“个人收入”，且必须是同一问题的多年对比"}
        if table1 != '1' and table2 != '1' and table3 != '1':  # 选了三列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            col3_eng = col_names[table3[0:4]][table3][col3_cn][1]
            if type1 == 'a' and type2 == 'a' and type3 == 'a' and region == '1':  # 南北；三个均为计算平均值型
                pass
            if type1 == 'a' and type2 == 'a' and type3 == 'a' and region == '2':  # 东中西；三个均为计算平均值型
                pass
            else:
                return {"status": "failure", "reason": "若绘制多系列盒须图，请选择两列或两列以上可计算数值型的数据，如“个人收入”，且必须是同一问题的多年对比"}
        else:
            return {"status": "failure", "reason": "若绘制多系列盒须图，请选择两列或两列以上可计算数值型的数据，如“个人收入”，且必须是同一问题的多年对比"}
    if tubiao == '19' or tubiao == '20' or tubiao == '21':  # 堆积条形图、堆积柱状图、极坐标堆积柱状图
        if table1 != '1' and table2 == '1' and table3 == '1':  # 只选了一列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            if region == '1':  # 南北
                return nab_nsecw_count192021(['ns', {table1: [col1_eng, type1]}, tubiao, username])
            if region == '2':  # 东中西
                return nab_nsecw_count192021(['ecw', {table1: [col1_eng, type1]}, tubiao, username])
        if table1 != '1' and table2 != '1' and table3 == '1':  # 选了两列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            if region == '1':  # 南北
                return nab_nsecw_count192021(['ns', {table1: [col1_eng, type1], table2: [col2_eng, type2]}, tubiao, username])
            if region == '2':  # 东中西
                return nab_nsecw_count192021(['ecw', {table1: [col1_eng, type1], table2: [col2_eng, type2]}, tubiao, username])
        if table1 != '1' and table2 != '1' and table3 != '1':  # 选了三列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            col3_eng = col_names[table3[0:4]][table3][col3_cn][1]
            if region == '1':  # 南北
                return nab_nsecw_count192021(['ns', {table1: [col1_eng, type1], table2: [col2_eng, type2], table3: [col3_eng, type3]}, tubiao, username])
            if region == '2':  # 东中西
                return nab_nsecw_count192021(['ecw', {table1: [col1_eng, type1], table2: [col2_eng, type2], table3: [col3_eng, type3]}, tubiao, username])
    if tubiao == '22':  # 堆积百分比柱状图
        if table1 != '1' and table2 == '1' and table3 == '1':  # 只选了一列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            if region == '1':  # 南北
                return nab_nsecw_count22(['ns', {table1: [col1_eng, type1]}, username])
            if region == '2':  # 东中西
                return nab_nsecw_count22(['ecw', {table1: [col1_eng, type1]}, username])
        if table1 != '1' and table2 != '1' and table3 == '1':  # 选了两列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            if region == '1':  # 南北
                return nab_nsecw_count22(['ns', {table1: [col1_eng, type1], table2: [col2_eng, type2]}, username])
            if region == '2':  # 东中西
                return nab_nsecw_count22(['ecw', {table1: [col1_eng, type1], table2: [col2_eng, type2]}, username])
        if table1 != '1' and table2 != '1' and table3 != '1':  # 选了三列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            col2_eng = col_names[table2[0:4]][table2][col2_cn][1]
            col3_eng = col_names[table3[0:4]][table3][col3_cn][1]
            if region == '1':  # 南北
                return nab_nsecw_count22(['ns', {table1: [col1_eng, type1], table2: [col2_eng, type2], table3: [col3_eng, type3]}, username])
            if region == '2':  # 东中西
                return nab_nsecw_count22(['ecw', {table1: [col1_eng, type1], table2: [col2_eng, type2], table3: [col3_eng, type3]}, username])
    if tubiao == '23':  # 三维柱状图
        if table1 != '1' and table2 == '1' and table3 == '1':  # 只选了一列数据
            col1_eng = col_names[table1[0:4]][table1][col1_cn][1]
            if type1 == 'b' and region == '1':  # 南北；比例型
                return b_ns_count23(table1, col1_eng, username)
            if type1 == 'b' and region == '2':  # 东中西；比例型
                return b_ecw_count23(table1, col1_eng, username)
            else:
                return {"status": "failure", "reason": "若绘制3D柱状图，请选择一列可计算比例型的数据，如“您家做饭用的水最主要是”"}
        else:
            return {"status": "failure", "reason": "若绘制3D柱状图，请选择一列可计算比例型的数据，如“您家做饭用的水最主要是”"}
