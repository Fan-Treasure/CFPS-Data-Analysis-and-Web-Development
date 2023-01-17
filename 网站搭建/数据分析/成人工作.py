import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CPFS2018'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM job')
data_2018 = mycursor.fetchall()


#成人工作
#农村
work_2018_v=data_2018.egc203_a_1[data_2018["typ_hk"]=='乡村'].dropna().tolist()
#work_2018_v=deleteElem(work_2018_v,-8)

#城市
work_2018_c=data_2018.egc203_a_1[data_2018["typ_hk"]=='城镇'].dropna().tolist()
#work_2018_c=deleteElem(out_2018_c,-8)
ind=np.arange(0,15,3)
width=0.5
color=['red','blue','green','red','blue','green']
# x1=[np.mean(work_2018_v),np.mean(out_2012_v),np.mean(out_2014_v),np.mean(out_2016_v),np.mean(out_2018_v)]
# x2=[np.mean(work_2018_v),np.mean(out_2012_c),np.mean(out_2014_c),np.mean(out_2016_c),np.mean(out_2018_c)]

plt.bar(ind,work_2018_v,width,align='edge',label='农村')
plt.bar(ind+width,work_2018_c,width,align='edge',label='城市')

#plt.xticks(ind, ('2010', '2012', '2014', '2016', '2018'))
plt.legend()
#plt.title("城乡家庭总支出对比")
plt.show()

#农村城市南北部东中西部对比
ind=np.arange(0,12,2)
width=0.3
color=['red','blue','green','red','blue','green']
#南

plt.bar(ind+3*width,work_2018_v,width,align='edge',color="red",edgecolor="grey")
#北
plt.bar(ind+3*width,work_2018_v,width,align='edge',bottom=work_2018_c,color="blue",edgecolor="grey")
plt.xticks(ind, ('政府', '事业', '国企', '私营/个体', '外商'))
plt.legend()
plt.title("城镇")
plt.show()
#东中西部
plt.bar(ind,work_2018_v,width,align='edge',label='南部地区',color="red",edgecolor="grey")
plt.bar(ind+width,work_2018_v,width,align='edge',color="red",edgecolor="grey",label="北部地区")
plt.bar(ind+2*width,work_2018_v,width,align='edge',color="red",edgecolor="grey")
plt.bar(ind+3*width,work_2018_v,width,align='edge',color="red",edgecolor="grey")
#
plt.bar(ind,work_2018_c,width,align='edge',bottom=work_2018_c,color="blue",label="东部地区",edgecolor="grey")
plt.bar(ind+width,work_2018_c,width,align='edge',bottom=work_2018_c,color="blue",edgecolor="grey",label="中部地区")
plt.bar(ind+2*width,work_2018_c,width,align='edge',bottom=work_2018_c,color="blue",edgecolor="grey",label="西部地区")
plt.bar(ind+3*width,work_2018_c,width,align='edge',bottom=work_2018_c,color="blue",edgecolor="grey")
plt.xticks(ind, ('政府', '事业', '国企', '私营/个体', '外商'))
plt.legend()
plt.title("农村")
plt.show()