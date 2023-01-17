from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CFPS2018'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM education')
data_2018 = mycursor.fetchall()

#城乡对比
edu_2018_v = data_2018.w01[data_2018["typ_hk"] == '乡村'].tolist()
edu_2018_c = data_2018.w01[data_2018["typ_hk"] == '城镇'].tolist()
edu_typ = [0, 3, 4, 5, 6, 7, 8, 9]  # 教育阶段

edu_count_0, edu_count_3, edu_count_4, edu_count_5, edu_count_6, edu_count_7, edu_count_8, edu_count_9, edu_count_10 = [], [], [], [], [], [], [], [], []  # 不同教育阶段人数百分比

edu_count_0_v = [Counter(edu_2018_v)[edu_typ[0]] / len(edu_2018_v)]
edu_count_3_v = [Counter(edu_2018_v)[edu_typ[1]] / len(edu_2018_v)]
edu_count_4_v = [Counter(edu_2018_v)[edu_typ[2]] / len(edu_2018_v)]
edu_count_5_v = [Counter(edu_2018_v)[edu_typ[3]] / len(edu_2018_v)]
edu_count_6_v = [Counter(edu_2018_v)[edu_typ[4]] / len(edu_2018_v)]
edu_count_7_v = [Counter(edu_2018_v)[edu_typ[5]] / len(edu_2018_v)]
edu_count_8_v = [Counter(edu_2018_v)[edu_typ[6]] / len(edu_2018_v)]
edu_count_9_v = [Counter(edu_2018_v)[edu_typ[7]] / len(edu_2018_v)]
edu_count_0_c = [Counter(edu_2018_c)[edu_typ[0]] / len(edu_2018_c)]
edu_count_3_c = [Counter(edu_2018_c)[edu_typ[1]] / len(edu_2018_c)]
edu_count_4_c = [Counter(edu_2018_c)[edu_typ[2]] / len(edu_2018_c)]
edu_count_5_c = [Counter(edu_2018_c)[edu_typ[3]] / len(edu_2018_c)]
edu_count_6_c = [Counter(edu_2018_c)[edu_typ[4]] / len(edu_2018_c)]
edu_count_7_c = [Counter(edu_2018_c)[edu_typ[5]] / len(edu_2018_c)]
edu_count_8_c = [Counter(edu_2018_c)[edu_typ[6]] / len(edu_2018_c)]
edu_count_9_c = [Counter(edu_2018_c)[edu_typ[7]] / len(edu_2018_c)]

ind=np.arange(0,3,1.5)
width=0.3
color=['red','blue','green','yellow','pink','orange','skyblue','purple']
#文盲/半文盲
plt.bar(ind,edu_count_0_v,width,align='edge',label='文盲/半文盲',color="red",edgecolor="grey")
plt.bar(ind+width,edu_count_0_c,width,align='edge',color="red",edgecolor="grey")

#小学
plt.bar(ind,edu_count_3_v,width,align='edge',label='小学',bottom=edu_count_0_v,color="blue",edgecolor="grey")
plt.bar(ind+width,edu_count_3_c,width,align='edge',bottom=edu_count_0_c,color="blue",edgecolor="grey")

#初中
bot=[[],[]]#底，对应农村城市
bot[0].append(edu_count_0_v[0]+edu_count_3_v[0])
bot[1].append(edu_count_0_c[0]+edu_count_3_c[0])
plt.bar(ind,edu_count_4_v,width,align='edge',bottom=bot[0],color="green",edgecolor="grey",label="初中")
plt.bar(ind+width,edu_count_4_c,width,align='edge',bottom=bot[1],color="green",edgecolor="grey")

#高中/中专/技校/职高
bot[0][0] += edu_count_4_v[0]
bot[1][0] += edu_count_4_c[0]
plt.bar(ind,edu_count_5_v,width,align='edge',bottom=bot[0],color="yellow",edgecolor="grey",label="高中/中专/技校/职高")
plt.bar(ind+width,edu_count_5_c,width,align='edge',bottom=bot[1],color="yellow",edgecolor="grey")

#大专
bot[0][0] += edu_count_5_v[0]
bot[1][0] += edu_count_5_c[0]
plt.bar(ind,edu_count_6_v,width,align='edge',bottom=bot[0],color="pink",edgecolor="grey",label="大专")
plt.bar(ind+width,edu_count_6_c,width,align='edge',bottom=bot[1],color="pink",edgecolor="grey")

#大学本科
bot[0][0] += edu_count_6_v[0]
bot[1][0] += edu_count_6_c[0]
plt.bar(ind,edu_count_7_v,width,align='edge',bottom=bot[0],color="orange",edgecolor="grey",label="大学本科")
plt.bar(ind+width,edu_count_7_c,width,align='edge',bottom=bot[1],color="orange",edgecolor="grey")

#硕士
bot[0][0] += edu_count_7_v[0]
bot[1][0] += edu_count_7_c[0]
plt.bar(ind,edu_count_8_v,width,align='edge',bottom=bot[0],color="skyblue",edgecolor="grey",label="硕士")
plt.bar(ind+width,edu_count_8_c,width,align='edge',bottom=bot[1],color="skyblue",edgecolor="grey")

#博士
bot[0][0] += edu_count_8_v[0]
bot[1][0] += edu_count_8_c[0]
plt.bar(ind,edu_count_9_v,width,align='edge',bottom=bot[0],color="purple",edgecolor="grey",label="博士")
plt.bar(ind+width,edu_count_9_c,width,align='edge',bottom=bot[1],color="purple",edgecolor="grey")

plt.xticks(ind, ('农村', '城市'))
plt.legend()
plt.title("城乡居民教育受教育阶段")
plt.savefig("../图表/城乡居民教育受教育阶段.png")
plt.show()