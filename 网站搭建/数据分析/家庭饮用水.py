from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mysql.connector

plt.cla()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CFPS2010'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM water')
data_2010 = mycursor.fetchall()

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CFPS2012'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM water')
data_2012 = mycursor.fetchall()

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CFPS2014'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM water')
data_2014 = mycursor.fetchall()

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CFPS2016'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM water')
data_2016 = mycursor.fetchall()

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CFPS2018'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM water')
data_2018 = mycursor.fetchall()


# 农村
water_2010_v = data_2010.fb1[data_2010["typ_hk"] == '乡村'].tolist()
water_2012_v = data_2012.fb1[data_2012["typ_hk"] == '乡村'].tolist()
water_2014_v = data_2014.fa3[data_2014["typ_hk"] == '乡村'].tolist()
water_2016_v = data_2016.fa3[data_2016["typ_hk"] == '乡村'].tolist()
water_2018_v = data_2018.fa3[data_2018["typ_hk"] == '乡村'].tolist()

water_2012_v = list(map(int, pd.Series(water_2012_v).dropna()))
water_2014_v = list(map(int, pd.Series(water_2014_v).dropna()))

# 城镇
water_2010_c = data_2010.fb1[data_2010["typ_hk"] == '城镇'].tolist()
water_2012_c = data_2012.fb1[data_2012["typ_hk"] == '城镇'].tolist()
water_2014_c = data_2014.fa3[data_2014["typ_hk"] == '城镇'].tolist()
water_2016_c = data_2016.fa3[data_2016["typ_hk"] == '城镇'].tolist()
water_2018_c = data_2018.fa3[data_2018["typ_hk"] == '城镇'].tolist()

water_2012_c = list(map(int, pd.Series(water_2012_c).dropna()))
water_2014_c = list(map(int, pd.Series(water_2014_c).dropna()))
water_typ = [3, 2, 5, 1, 4, 6]  # 饮用水类型
water_count_2010_v, water_count_2012_v, water_count_2014_v, water_count_2016_v, water_count_2018_v = [], [], [], [], []  # 农村不同类型饮用水数量
water_count_2010_c, water_count_2012_c, water_count_2014_c, water_count_2016_c, water_count_2018_c = [], [], [], [], []  # 城镇不同类型饮用水数量
for i in range(6):
    # 农村
    water_count_2010_v.append((Counter(water_2010_v)[water_typ[i]]) / len(water_2010_v))
    water_count_2012_v.append((Counter(water_2012_v)[water_typ[i]]) / len(water_2012_v))
    water_count_2014_v.append((Counter(water_2014_v)[water_typ[i]]) / len(water_2014_v))
    water_count_2016_v.append((Counter(water_2016_v)[water_typ[i]]) / len(water_2016_v))
    water_count_2018_v.append((Counter(water_2018_v)[water_typ[i]]) / len(water_2018_v))
    # 城镇
    water_count_2010_c.append((Counter(water_2010_c)[water_typ[i]]) / len(water_2010_c))
    water_count_2012_c.append((Counter(water_2012_c)[water_typ[i]]) / len(water_2012_c))
    water_count_2014_c.append((Counter(water_2014_c)[water_typ[i]]) / len(water_2014_c))
    water_count_2016_c.append((Counter(water_2016_c)[water_typ[i]]) / len(water_2016_c))
    water_count_2018_c.append((Counter(water_2018_c)[water_typ[i]]) / len(water_2018_c))


ind=np.arange(0,13.2,2.2)
width=0.3
color=['red','blue','green','red','blue','green']
plt.bar(ind,water_count_2010_v,width,align='edge',label='2010')
plt.bar(ind+width,water_count_2012_v,width,align='edge',label='2012')
plt.bar(ind+2*width,water_count_2014_v,width,align='edge',label='2014')
plt.bar(ind+3*width,water_count_2016_v,width,align='edge',label='2016')
plt.bar(ind+4*width,water_count_2018_v,width,align='edge',label='2018')
plt.xticks(ind, ('自来水', '井水', '雨水', '江河湖水', '桶装水/纯净水/过滤水', '窖水'))
plt.legend()
plt.title("农村")
plt.savefig("../图表/农村家庭饮用水类型跨年对比.png")
plt.show()


ind=np.arange(0,13.2,2.2)
width=0.3
color=['red','blue','green','red','blue','green']
plt.bar(ind,water_count_2010_c,width,align='edge',label='2010')
plt.bar(ind+width,water_count_2012_c,width,align='edge',label='2012')
plt.bar(ind+2*width,water_count_2014_c,width,align='edge',label='2014')
plt.bar(ind+3*width,water_count_2016_c,width,align='edge',label='2016')
plt.bar(ind+4*width,water_count_2018_c,width,align='edge',label='2018')
plt.xticks(ind, ('自来水', '井水', '雨水', '江河湖水', '桶装水/纯净水/过滤水', '窖水'))
plt.legend()
plt.title("城镇")
plt.savefig("../图表/城镇家庭饮用水类型跨年对比.png")
plt.show()


#农村南
water_2010_v_s=data_2010.fb1[(data_2010["typ_hk"]=='乡村')&(data_2010["N_S"]=="S")].tolist()
water_2012_v_s=data_2012.fb1[(data_2012["typ_hk"]=='乡村')&(data_2012["N_S"]=="S")].tolist()
water_2014_v_s=data_2014.fa3[(data_2014["typ_hk"]=='乡村')&(data_2014["N_S"]=="S")].tolist()
water_2016_v_s=data_2016.fa3[(data_2016["typ_hk"]=='乡村')&(data_2016["N_S"]=="S")].tolist()
water_2018_v_s=data_2018.fa3[(data_2018["typ_hk"]=='乡村')&(data_2018["N_S"]=="S")].tolist()

water_2012_v_s=list(map(int,pd.Series(water_2012_v_s).dropna()))
water_2014_v_s=list(map(int,pd.Series(water_2014_v_s).dropna()))
#农村北
water_2010_v_n=data_2010.fb1[(data_2010["typ_hk"]=='乡村') &(data_2010["N_S"]=="N")].tolist()
water_2012_v_n=data_2012.fb1[(data_2012["typ_hk"]=='乡村')&(data_2012["N_S"]=="N")].tolist()
water_2014_v_n=data_2014.fa3[(data_2014["typ_hk"]=='乡村')&(data_2014["N_S"]=="N")].tolist()
water_2016_v_n=data_2016.fa3[(data_2016["typ_hk"]=='乡村')&(data_2016["N_S"]=="N")].tolist()
water_2018_v_n=data_2018.fa3[(data_2018["typ_hk"]=='乡村') &(data_2018["N_S"]=="N")].tolist()

water_2012_v_n=list(map(int,pd.Series(water_2012_v_n).dropna()))
water_2014_v_n=list(map(int,pd.Series(water_2014_v_n).dropna()))

water_typ=[3,2,5,1,4,6]#饮用水类型
water_count_2010_v_s,water_count_2012_v_s,water_count_2014_v_s,water_count_2016_v_s,water_count_2018_v_s=[],[],[],[],[]#农村不同类型饮用水数量
water_count_2010_v_n,water_count_2012_v_n,water_count_2014_v_n,water_count_2016_v_n,water_count_2018_v_n=[],[],[],[],[]#农村不同类型饮用水数量
for i in range(6):
    #农村南
    water_count_2010_v_s.append((Counter(water_2010_v_s)[water_typ[i]])/len(water_2010_v))
    water_count_2012_v_s.append((Counter(water_2012_v_s)[water_typ[i]])/len(water_2012_v))
    water_count_2014_v_s.append((Counter(water_2014_v_s)[water_typ[i]])/len(water_2014_v))
    water_count_2016_v_s.append((Counter(water_2016_v_s)[water_typ[i]])/len(water_2016_v))
    water_count_2018_v_s.append((Counter(water_2018_v_s)[water_typ[i]])/len(water_2018_v))
    #农村北
    water_count_2010_v_n.append((Counter(water_2010_v_n)[water_typ[i]])/len(water_2010_v))
    water_count_2012_v_n.append((Counter(water_2012_v_n)[water_typ[i]])/len(water_2012_v))
    water_count_2014_v_n.append((Counter(water_2014_v_n)[water_typ[i]])/len(water_2014_v))
    water_count_2016_v_n.append((Counter(water_2016_v_n)[water_typ[i]])/len(water_2016_v))
    water_count_2018_v_n.append((Counter(water_2018_v_n)[water_typ[i]])/len(water_2018_v))

ind=np.arange(0,13.2,2.2)
width=0.3
color=['red','blue','green','red','blue','green']
#南
plt.bar(ind,water_count_2010_v_s,width,align='edge',label='南部地区',color="red",edgecolor="grey")
plt.bar(ind+width,water_count_2012_v_s,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_v_s,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_v_s,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_v_s,width,align='edge',color="red",edgecolor="grey")
#北
plt.bar(ind,water_count_2010_v_n,width,align='edge',bottom=water_count_2010_v_s,color="blue",label="北部地区",edgecolor="grey")
plt.bar(ind+width,water_count_2012_v_n,width,align='edge',bottom=water_count_2012_v_s,color="blue",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_v_n,width,align='edge',bottom=water_count_2014_v_s,color="blue",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_v_n,width,align='edge',bottom=water_count_2016_v_s,color="blue",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_v_n,width,align='edge',bottom=water_count_2018_v_s,color="blue",edgecolor="grey")
plt.xticks(ind, ('自来水', '井水', '雨水', '江湖水', '纯净水', '窖水'))
plt.legend()
plt.title("农村")
plt.savefig("../图表/农村家庭饮用水类型南北对比.png")
plt.show()


#城镇南
water_2010_c_s=data_2010.fb1[(data_2010["typ_hk"]=='城镇') &(data_2010["N_S"]=="S")].tolist()
water_2012_c_s=data_2012.fb1[(data_2012["typ_hk"]=='城镇')&(data_2012["N_S"]=="S")].tolist()
water_2014_c_s=data_2014.fa3[(data_2014["typ_hk"]=='城镇')&(data_2014["N_S"]=="S")].tolist()
water_2016_c_s=data_2016.fa3[(data_2016["typ_hk"]=='城镇')&(data_2016["N_S"]=="S")].tolist()
water_2018_c_s=data_2018.fa3[(data_2018["typ_hk"]=='城镇') &(data_2018["N_S"]=="S")].tolist()

water_2012_c_s=list(map(int,pd.Series(water_2012_c_s).dropna()))
water_2014_c_s=list(map(int,pd.Series(water_2014_c_s).dropna()))
#城镇北
water_2010_c_n=data_2010.fb1[(data_2010["typ_hk"]=='城镇') &(data_2010["N_S"]=="N")].tolist()
water_2012_c_n=data_2012.fb1[(data_2012["typ_hk"]=='城镇')&(data_2012["N_S"]=="N")].tolist()
water_2014_c_n=data_2014.fa3[(data_2014["typ_hk"]=='城镇')&(data_2014["N_S"]=="N")].tolist()
water_2016_c_n=data_2016.fa3[(data_2016["typ_hk"]=='城镇')&(data_2016["N_S"]=="N")].tolist()
water_2018_c_n=data_2018.fa3[(data_2018["typ_hk"]=='城镇') &(data_2018["N_S"]=="N")].tolist()

water_2012_c_n=list(map(int,pd.Series(water_2012_c_n).dropna()))
water_2014_c_n=list(map(int,pd.Series(water_2014_c_n).dropna()))

water_typ=[3,2,5,1,4,6]#饮用水类型
water_count_2010_c_s,water_count_2012_c_s,water_count_2014_c_s,water_count_2016_c_s,water_count_2018_c_s=[],[],[],[],[]#农村不同类型饮用水数量
water_count_2010_c_n,water_count_2012_c_n,water_count_2014_c_n,water_count_2016_c_n,water_count_2018_c_n=[],[],[],[],[]#农村不同类型饮用水数量
for i in range(6):
    #农村南
    water_count_2010_c_s.append((Counter(water_2010_c_s)[water_typ[i]])/len(water_2010_c))
    water_count_2012_c_s.append((Counter(water_2012_c_s)[water_typ[i]])/len(water_2012_c))
    water_count_2014_c_s.append((Counter(water_2014_c_s)[water_typ[i]])/len(water_2014_c))
    water_count_2016_c_s.append((Counter(water_2016_c_s)[water_typ[i]]) / len(water_2016_c))
    water_count_2018_c_s.append((Counter(water_2018_c_s)[water_typ[i]])/len(water_2018_c))
    #农村北
    water_count_2010_c_n.append((Counter(water_2010_c_n)[water_typ[i]])/len(water_2010_c))
    water_count_2012_c_n.append((Counter(water_2012_c_n)[water_typ[i]])/len(water_2012_c))
    water_count_2014_c_n.append((Counter(water_2014_c_n)[water_typ[i]])/len(water_2014_c))
    water_count_2016_c_n.append((Counter(water_2016_c_n)[water_typ[i]]) / len(water_2016_c))
    water_count_2018_c_n.append((Counter(water_2018_c_n)[water_typ[i]])/len(water_2018_c))
###########
ind=np.arange(0,13.2,2.2)
width=0.3
color=['red','blue','green','red','blue','green']
#南
plt.bar(ind,water_count_2010_c_s,width,align='edge',label='南部地区',color="red",edgecolor="grey")
plt.bar(ind+width,water_count_2012_c_s,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_c_s,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_c_s,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_c_s,width,align='edge',color="red",edgecolor="grey")
#北
plt.bar(ind,water_count_2010_c_n,width,align='edge',bottom=water_count_2010_c_s,color="blue",label="北部地区",edgecolor="grey")
plt.bar(ind+width,water_count_2012_c_n,width,align='edge',bottom=water_count_2012_c_s,color="blue",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_c_n,width,align='edge',bottom=water_count_2014_c_s,color="blue",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_c_n,width,align='edge',bottom=water_count_2018_c_s,color="blue",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_c_n,width,align='edge',bottom=water_count_2018_c_s,color="blue",edgecolor="grey")
plt.xticks(ind, ('自来水', '井水', '雨水', '江湖水', '纯净水', '窖水'))
plt.legend()
plt.title("城镇")
plt.savefig("../图表/城镇家庭饮用水类型南北对比.png")
plt.show()


# 农村东 中 西 东北部对比
#农村东
water_2010_v_e=data_2010.fb1[(data_2010["typ_hk"]=='乡村') &(data_2010["E_C_W_EW"]=="E")].tolist()
water_2012_v_e=data_2012.fb1[(data_2012["typ_hk"]=='乡村')&(data_2012["E_C_W_EW"]=="E")].tolist()
water_2014_v_e=data_2014.fa3[(data_2014["typ_hk"]=='乡村')&(data_2014["E_C_W_EW"]=="E")].tolist()
water_2016_v_e=data_2016.fa3[(data_2016["typ_hk"]=='乡村')&(data_2016["E_C_W_EW"]=="E")].tolist()
water_2018_v_e=data_2018.fa3[(data_2018["typ_hk"]=='乡村') &(data_2018["E_C_W_EW"]=="E")].tolist()

water_2012_v_e=list(map(int,pd.Series(water_2012_v_e).dropna()))
water_2014_v_e=list(map(int,pd.Series(water_2014_v_e).dropna()))
#农村中
water_2010_v_c=data_2010.fb1[(data_2010["typ_hk"]=='乡村') &(data_2010["E_C_W_EW"]=="C")].tolist()
water_2012_v_c=data_2012.fb1[(data_2012["typ_hk"]=='乡村')&(data_2012["E_C_W_EW"]=="C")].tolist()
water_2014_v_c=data_2014.fa3[(data_2014["typ_hk"]=='乡村')&(data_2014["E_C_W_EW"]=="C")].tolist()
water_2016_v_c=data_2016.fa3[(data_2016["typ_hk"]=='乡村')&(data_2016["E_C_W_EW"]=="C")].tolist()
water_2018_v_c=data_2018.fa3[(data_2018["typ_hk"]=='乡村') &(data_2018["E_C_W_EW"]=="C")].tolist()

water_2012_v_c=list(map(int,pd.Series(water_2012_v_c).dropna()))
water_2014_v_c=list(map(int,pd.Series(water_2014_v_c).dropna()))

#农村西部
water_2010_v_w=data_2010.fb1[(data_2010["typ_hk"]=='乡村') &(data_2010["E_C_W_EW"]=="W")].tolist()
water_2012_v_w=data_2012.fb1[(data_2012["typ_hk"]=='乡村')&(data_2012["E_C_W_EW"]=="W")].tolist()
water_2014_v_w=data_2014.fa3[(data_2014["typ_hk"]=='乡村')&(data_2014["E_C_W_EW"]=="W")].tolist()
water_2016_v_w=data_2016.fa3[(data_2016["typ_hk"]=='乡村')&(data_2016["E_C_W_EW"]=="W")].tolist()
water_2018_v_w=data_2018.fa3[(data_2018["typ_hk"]=='乡村') &(data_2018["E_C_W_EW"]=="W")].tolist()

water_2012_v_w=list(map(int,pd.Series(water_2012_v_w).dropna()))
water_2014_v_w=list(map(int,pd.Series(water_2014_v_w).dropna()))

#农村东北部
water_2010_v_ew=data_2010.fb1[(data_2010["typ_hk"]=='乡村') &(data_2010["E_C_W_EW"]=="EW")].tolist()
water_2012_v_ew=data_2012.fb1[(data_2012["typ_hk"]=='乡村')&(data_2012["E_C_W_EW"]=="EW")].tolist()
water_2014_v_ew=data_2014.fa3[(data_2014["typ_hk"]=='乡村')&(data_2014["E_C_W_EW"]=="EW")].tolist()
water_2016_v_ew=data_2016.fa3[(data_2016["typ_hk"]=='乡村')&(data_2016["E_C_W_EW"]=="EW")].tolist()
water_2018_v_ew=data_2018.fa3[(data_2018["typ_hk"]=='乡村') &(data_2018["E_C_W_EW"]=="EW")].tolist()

water_2012_v_ew=list(map(int,pd.Series(water_2012_v_ew).dropna()))
water_2014_v_ew=list(map(int,pd.Series(water_2014_v_ew).dropna()))

water_typ=[3,2,5,1,4,6]#饮用水类型
water_count_2010_v_e,water_count_2012_v_e,water_count_2014_v_e,water_count_2016_v_e,water_count_2018_v_e=[],[],[],[],[]#农村不同类型饮用水数量
water_count_2010_v_c,water_count_2012_v_c,water_count_2014_v_c,water_count_2016_v_c,water_count_2018_v_c=[],[],[],[],[]#农村不同类型饮用水数量
water_count_2010_v_w,water_count_2012_v_w,water_count_2014_v_w,water_count_2016_v_w,water_count_2018_v_w=[],[],[],[],[]#农村不同类型饮用水数量
water_count_2010_v_ew,water_count_2012_v_ew,water_count_2014_v_ew,water_count_2016_v_ew,water_count_2018_v_ew=[],[],[],[],[]#农村不同类型饮用水数量
for i in range(6):
    #农村东
    water_count_2010_v_e.append((Counter(water_2010_v_e)[water_typ[i]])/len(water_2010_v))
    water_count_2012_v_e.append((Counter(water_2012_v_e)[water_typ[i]])/len(water_2012_v))
    water_count_2014_v_e.append((Counter(water_2014_v_e)[water_typ[i]])/len(water_2014_v))
    water_count_2016_v_e.append((Counter(water_2016_v_e)[water_typ[i]]) / len(water_2016_v))
    water_count_2018_v_e.append((Counter(water_2018_v_e)[water_typ[i]])/len(water_2018_v))
    #农村中
    water_count_2010_v_c.append((Counter(water_2010_v_c)[water_typ[i]])/len(water_2010_v))
    water_count_2012_v_c.append((Counter(water_2012_v_c)[water_typ[i]])/len(water_2012_v))
    water_count_2014_v_c.append((Counter(water_2014_v_c)[water_typ[i]])/len(water_2014_v))
    water_count_2016_v_c.append((Counter(water_2016_v_c)[water_typ[i]]) / len(water_2016_v))
    water_count_2018_v_c.append((Counter(water_2018_v_c)[water_typ[i]])/len(water_2018_v))
      #农村西
    water_count_2010_v_w.append((Counter(water_2010_v_w)[water_typ[i]])/len(water_2010_v))
    water_count_2012_v_w.append((Counter(water_2012_v_w)[water_typ[i]])/len(water_2012_v))
    water_count_2014_v_w.append((Counter(water_2014_v_w)[water_typ[i]])/len(water_2014_v))
    water_count_2016_v_w.append((Counter(water_2016_v_w)[water_typ[i]]) / len(water_2016_v))
    water_count_2018_v_w.append((Counter(water_2018_v_w)[water_typ[i]])/len(water_2018_v))
    # 农村东北
    water_count_2010_v_ew.append((Counter(water_2010_v_ew)[water_typ[i]]) / len(water_2010_v))
    water_count_2012_v_ew.append((Counter(water_2012_v_ew)[water_typ[i]]) / len(water_2012_v))
    water_count_2014_v_ew.append((Counter(water_2014_v_ew)[water_typ[i]]) / len(water_2014_v))
    water_count_2016_v_ew.append((Counter(water_2016_v_ew)[water_typ[i]]) / len(water_2016_v))
    water_count_2018_v_ew.append((Counter(water_2018_v_ew)[water_typ[i]]) / len(water_2018_v))
#######################
ind=np.arange(0,13.2,2.2)
width=0.3
color=['red','blue','green','red','blue','green']
#东
plt.bar(ind,water_count_2010_v_e,width,align='edge',label='东部地区',color="red",edgecolor="grey")
plt.bar(ind+width,water_count_2012_v_e,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_v_e,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_v_e,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_v_e,width,align='edge',color="red",edgecolor="grey")
#中
plt.bar(ind,water_count_2010_v_c,width,align='edge',bottom=water_count_2010_v_e,color="blue",label="中部地区",edgecolor="grey")
plt.bar(ind+width,water_count_2012_v_c,width,align='edge',bottom=water_count_2012_v_e,color="blue",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_v_c,width,align='edge',bottom=water_count_2014_v_e,color="blue",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_v_c,width,align='edge',bottom=water_count_2016_v_e,color="blue",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_v_c,width,align='edge',bottom=water_count_2018_v_e,color="blue",edgecolor="grey")
#西
bot=[[],[],[],[],[]]#底，对应五年
for i in range(6):
    bot[0].append(water_count_2010_v_e[i]+water_count_2010_v_c[i])
    bot[1].append(water_count_2012_v_e[i]+water_count_2012_v_c[i])
    bot[2].append(water_count_2014_v_e[i]+water_count_2014_v_c[i])
    bot[3].append(water_count_2016_v_e[i]+water_count_2016_v_c[i])
    bot[4].append(water_count_2018_v_e[i] + water_count_2018_v_c[i])

plt.bar(ind,water_count_2010_v_w,width,align='edge',bottom=bot[0],color="green",edgecolor="grey",label="西部地区")
plt.bar(ind+width,water_count_2012_v_w,width,align='edge',bottom=bot[1],color="green",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_v_w,width,align='edge',bottom=bot[2],color="green",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_v_w,width,align='edge',bottom=bot[3],color="green",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_v_w,width,align='edge',bottom=bot[4],color="green",edgecolor="grey")
#东北
bot=[[],[],[],[],[]]#底，对应五年
for i in range(6):
    bot[0].append(water_count_2010_v_e[i]+water_count_2010_v_c[i]+water_count_2010_v_w[i])
    bot[1].append(water_count_2012_v_e[i]+water_count_2012_v_c[i]+water_count_2012_v_w[i])
    bot[2].append(water_count_2014_v_e[i]+water_count_2014_v_c[i]+water_count_2014_v_w[i])
    bot[3].append(water_count_2016_v_e[i]+water_count_2016_v_c[i]+water_count_2016_v_w[i])
    bot[4].append(water_count_2018_v_e[i] + water_count_2018_v_c[i]+water_count_2018_v_w[i])

plt.bar(ind,water_count_2010_v_ew,width,align='edge',bottom=bot[0],color="yellow",edgecolor="grey",label="东北部地区")
plt.bar(ind+width,water_count_2012_v_ew,width,align='edge',bottom=bot[1],color="yellow",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_v_ew,width,align='edge',bottom=bot[2],color="yellow",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_v_ew,width,align='edge',bottom=bot[3],color="yellow",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_v_ew,width,align='edge',bottom=bot[4],color="yellow",edgecolor="grey")
plt.xticks(ind, ('自来水', '井水', '雨水', '江湖水', '纯净水', '窖水'))
plt.legend()
plt.title("农村")
plt.savefig("../图表/农村家庭饮用水类型东中西东北对比.png")
plt.show()


# 城镇东 中 西部对比
#城镇东
water_2010_c_e=data_2010.fb1[(data_2010["typ_hk"]=='城镇') &(data_2010["E_C_W_EW"]=="E")].tolist()
water_2012_c_e=data_2012.fb1[(data_2012["typ_hk"]=='城镇')&(data_2012["E_C_W_EW"]=="E")].tolist()
water_2014_c_e=data_2014.fa3[(data_2014["typ_hk"]=='城镇')&(data_2014["E_C_W_EW"]=="E")].tolist()
water_2016_c_e=data_2016.fa3[(data_2016["typ_hk"]=='城镇')&(data_2016["E_C_W_EW"]=="E")].tolist()
water_2018_c_e=data_2018.fa3[(data_2018["typ_hk"]=='城镇') &(data_2018["E_C_W_EW"]=="E")].tolist()

water_2012_c_e=list(map(int,pd.Series(water_2012_c_e).dropna()))
water_2014_c_e=list(map(int,pd.Series(water_2014_c_e).dropna()))
#城镇中
water_2010_c_c=data_2010.fb1[(data_2010["typ_hk"]=='城镇') &(data_2010["E_C_W_EW"]=="C")].tolist()
water_2012_c_c=data_2012.fb1[(data_2012["typ_hk"]=='城镇')&(data_2012["E_C_W_EW"]=="C")].tolist()
water_2014_c_c=data_2014.fa3[(data_2014["typ_hk"]=='城镇')&(data_2014["E_C_W_EW"]=="C")].tolist()
water_2016_c_c=data_2016.fa3[(data_2016["typ_hk"]=='城镇')&(data_2016["E_C_W_EW"]=="C")].tolist()
water_2018_c_c=data_2018.fa3[(data_2018["typ_hk"]=='城镇') &(data_2018["E_C_W_EW"]=="C")].tolist()

water_2012_c_c=list(map(int,pd.Series(water_2012_c_c).dropna()))
water_2014_c_c=list(map(int,pd.Series(water_2014_c_c).dropna()))

#城镇西部
water_2010_c_w=data_2010.fb1[(data_2010["typ_hk"]=='城镇') &(data_2010["E_C_W_EW"]=="W")].tolist()
water_2012_c_w=data_2012.fb1[(data_2012["typ_hk"]=='城镇')&(data_2012["E_C_W_EW"]=="W")].tolist()
water_2014_c_w=data_2014.fa3[(data_2014["typ_hk"]=='城镇')&(data_2014["E_C_W_EW"]=="W")].tolist()
water_2016_c_w=data_2016.fa3[(data_2016["typ_hk"]=='城镇')&(data_2016["E_C_W_EW"]=="W")].tolist()
water_2018_c_w=data_2018.fa3[(data_2018["typ_hk"]=='城镇') &(data_2018["E_C_W_EW"]=="W")].tolist()

water_2012_c_w=list(map(int,pd.Series(water_2012_c_w).dropna()))
water_2014_c_w=list(map(int,pd.Series(water_2014_c_w).dropna()))

#城镇东北部
water_2010_c_ew=data_2010.fb1[(data_2010["typ_hk"]=='城镇') &(data_2010["E_C_W_EW"]=="EW")].tolist()
water_2012_c_ew=data_2012.fb1[(data_2012["typ_hk"]=='城镇')&(data_2012["E_C_W_EW"]=="EW")].tolist()
water_2014_c_ew=data_2014.fa3[(data_2014["typ_hk"]=='城镇')&(data_2014["E_C_W_EW"]=="EW")].tolist()
water_2016_c_ew=data_2016.fa3[(data_2016["typ_hk"]=='城镇')&(data_2016["E_C_W_EW"]=="EW")].tolist()
water_2018_c_ew=data_2018.fa3[(data_2018["typ_hk"]=='城镇') &(data_2018["E_C_W_EW"]=="EW")].tolist()

water_2012_c_ew=list(map(int,pd.Series(water_2012_c_ew).dropna()))
water_2014_c_ew=list(map(int,pd.Series(water_2014_c_ew).dropna()))

water_typ=[3,2,5,1,4,6]#饮用水类型
water_count_2010_c_e,water_count_2012_c_e,water_count_2014_c_e,water_count_2016_c_e,water_count_2018_c_e=[],[],[],[],[]#农村不同类型饮用水数量
water_count_2010_c_c,water_count_2012_c_c,water_count_2014_c_c,water_count_2016_c_c,water_count_2018_c_c=[],[],[],[],[]#农村不同类型饮用水数量
water_count_2010_c_w,water_count_2012_c_w,water_count_2014_c_w,water_count_2016_c_w,water_count_2018_c_w=[],[],[],[],[]#农村不同类型饮用水数量
water_count_2010_c_ew,water_count_2012_c_ew,water_count_2014_c_ew,water_count_2016_c_ew,water_count_2018_c_ew=[],[],[],[],[]#农村不同类型饮用水数量
for i in range(6):
    #农村东
    water_count_2010_c_e.append((Counter(water_2010_c_e)[water_typ[i]])/len(water_2010_c))
    water_count_2012_c_e.append((Counter(water_2012_c_e)[water_typ[i]])/len(water_2012_c))
    water_count_2014_c_e.append((Counter(water_2014_c_e)[water_typ[i]])/len(water_2014_c))
    water_count_2016_c_e.append((Counter(water_2016_c_e)[water_typ[i]]) / len(water_2016_c))
    water_count_2018_c_e.append((Counter(water_2018_c_e)[water_typ[i]])/len(water_2018_c))
    #农村中
    water_count_2010_c_c.append((Counter(water_2010_c_c)[water_typ[i]])/len(water_2010_c))
    water_count_2012_c_c.append((Counter(water_2012_c_c)[water_typ[i]])/len(water_2012_c))
    water_count_2014_c_c.append((Counter(water_2014_c_c)[water_typ[i]])/len(water_2014_c))
    water_count_2016_c_c.append((Counter(water_2016_c_c)[water_typ[i]]) / len(water_2016_c))
    water_count_2018_c_c.append((Counter(water_2018_c_c)[water_typ[i]])/len(water_2018_c))
      #农村西
    water_count_2010_c_w.append((Counter(water_2010_c_w)[water_typ[i]])/len(water_2010_c))
    water_count_2012_c_w.append((Counter(water_2012_c_w)[water_typ[i]])/len(water_2012_c))
    water_count_2014_c_w.append((Counter(water_2014_c_w)[water_typ[i]])/len(water_2014_c))
    water_count_2016_c_w.append((Counter(water_2016_c_w)[water_typ[i]]) / len(water_2016_c))
    water_count_2018_c_w.append((Counter(water_2018_c_w)[water_typ[i]])/len(water_2018_c))
    # 农村东北
    water_count_2010_c_ew.append((Counter(water_2010_c_ew)[water_typ[i]]) / len(water_2010_c))
    water_count_2012_c_ew.append((Counter(water_2012_c_ew)[water_typ[i]]) / len(water_2012_c))
    water_count_2014_c_ew.append((Counter(water_2014_c_ew)[water_typ[i]]) / len(water_2014_c))
    water_count_2016_c_ew.append((Counter(water_2016_c_ew)[water_typ[i]]) / len(water_2016_c))
    water_count_2018_c_ew.append((Counter(water_2018_c_ew)[water_typ[i]]) / len(water_2018_c))
#######################
ind=np.arange(0,13.2,2.2)
width=0.3
color=['red','blue','green','red','blue','green']
#东
plt.bar(ind,water_count_2010_c_e,width,align='edge',label='东部地区',color="red",edgecolor="grey")
plt.bar(ind+width,water_count_2012_c_e,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_c_e,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_c_e,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_c_e,width,align='edge',color="red",edgecolor="grey")
#中
plt.bar(ind,water_count_2010_c_c,width,align='edge',bottom=water_count_2010_c_e,color="blue",label="中部地区",edgecolor="grey")
plt.bar(ind+width,water_count_2012_c_c,width,align='edge',bottom=water_count_2012_c_e,color="blue",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_c_c,width,align='edge',bottom=water_count_2014_c_e,color="blue",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_c_c,width,align='edge',bottom=water_count_2016_c_e,color="blue",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_c_c,width,align='edge',bottom=water_count_2018_c_e,color="blue",edgecolor="grey")
#西
bot=[[],[],[],[],[]]#底
for i in range(6):
    bot[0].append(water_count_2010_c_e[i]+water_count_2010_c_c[i])
    bot[1].append(water_count_2012_c_e[i]+water_count_2012_c_c[i])
    bot[2].append(water_count_2014_c_e[i]+water_count_2014_c_c[i])
    bot[3].append(water_count_2016_c_e[i]+water_count_2016_c_c[i])
    bot[4].append(water_count_2018_c_e[i] + water_count_2018_c_c[i])

plt.bar(ind,water_count_2010_c_w,width,align='edge',bottom=bot[0],color="green",edgecolor="grey",label="西部地区")
plt.bar(ind+width,water_count_2012_c_w,width,align='edge',bottom=bot[1],color="green",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_c_w,width,align='edge',bottom=bot[2],color="green",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_c_w,width,align='edge',bottom=bot[3],color="green",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_c_w,width,align='edge',bottom=bot[4],color="green",edgecolor="grey")
#东北
bot=[[],[],[],[],[]]#底
for i in range(6):
    bot[0].append(water_count_2010_c_e[i]+water_count_2010_c_c[i]+water_count_2010_c_w[i])
    bot[1].append(water_count_2012_c_e[i]+water_count_2012_c_c[i]+water_count_2012_c_w[i])
    bot[2].append(water_count_2014_c_e[i]+water_count_2014_c_c[i]+water_count_2014_c_w[i])
    bot[3].append(water_count_2016_c_e[i]+water_count_2016_c_c[i]+water_count_2016_c_w[i])
    bot[4].append(water_count_2018_c_e[i] + water_count_2018_c_c[i]+water_count_2018_c_w[i])

plt.bar(ind,water_count_2010_c_ew,width,align='edge',bottom=bot[0],color="yellow",edgecolor="grey",label="东北部地区")
plt.bar(ind+width,water_count_2012_c_ew,width,align='edge',bottom=bot[1],color="yellow",edgecolor="grey")
plt.bar(ind+2*width,water_count_2014_c_ew,width,align='edge',bottom=bot[2],color="yellow",edgecolor="grey")
plt.bar(ind+3*width,water_count_2016_c_ew,width,align='edge',bottom=bot[3],color="yellow",edgecolor="grey")
plt.bar(ind+4*width,water_count_2018_c_ew,width,align='edge',bottom=bot[4],color="yellow",edgecolor="grey")
plt.xticks(ind, ('自来水', '井水', '雨水', '江湖水', '纯净水', '窖水'))
plt.legend()
plt.title("城镇")
plt.savefig("../图表/城镇家庭饮用水类型东中西东北对比.png")
plt.show()
