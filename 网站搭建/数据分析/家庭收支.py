import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import mysql.connector

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
mycursor.execute('SELECT * FROM income')
data_2010 = mycursor.fetchall()

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CFPS2012'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM income')
data_2012 = mycursor.fetchall()

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CFPS2014'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM income')
data_2014 = mycursor.fetchall()

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CFPS2016'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM income')
data_2016 = mycursor.fetchall()

# 连接数据库
mydb = mysql.connector.connect(
    host='',
    user='root',
    password='',
    database='CFPS2018'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM income')
data_2018 = mycursor.fetchall()


#删除函数
def deleteElem(original,val):
    j=0
    for i in range(len(original)):
        if original[i] != val:
            original[j]=original[i]
            j=j+1
    return original[0:j]


#农村收入
wage_2010_v=data_2010.ff601[data_2010["typ_hk"]=='乡村'].dropna().tolist()
wage_2012_v=data_2012.fincome1_adj[data_2012["typ_hk"]=='乡村'].dropna().tolist()
wage_2014_v=data_2014.fincome1[data_2014["typ_hk"]=='乡村'].dropna().tolist()
wage_2016_v=data_2016.fincome1[data_2016["typ_hk"]=='乡村'].dropna().tolist()
wage_2018_v=data_2018.fincome1[data_2018["typ_hk"]=='乡村'].dropna().tolist()
'''wage_2010_v=deleteElem(wage_2010_v,-8)
wage_2012_v=deleteElem(wage_2012_v,-8)
wage_2014_v=deleteElem(wage_2014_v,-8)
wage_2016_v=deleteElem(wage_2016_v,-8)
wage_2018_v=deleteElem(wage_2018_v,-8)'''

#人均收入
wage_per_2012_v=data_2012.fincome1_per_adj[data_2012["typ_hk"]=='乡村'].dropna().tolist()
wage_per_2014_v=data_2014.fincome1_per[data_2014["typ_hk"]=='乡村'].dropna().tolist()
wage_per_2016_v=data_2016.fincome1_per[data_2016["typ_hk"]=='乡村'].dropna().tolist()
wage_per_2018_v=data_2018.fincome1_per[data_2018["typ_hk"]=='乡村'].dropna().tolist()
'''wage_per_2012_v=deleteElem(wage_per_2012_v,-8)
wage_per_2014_v=deleteElem(wage_per_2014_v,-8)
wage_per_2016_v=deleteElem(wage_per_2016_v,-8)
wage_per_2018_v=deleteElem(wage_per_2018_v,-8)'''


#城市
wage_2010_c=data_2010.ff601[data_2010["typ_hk"]=='城镇'].dropna().tolist()
wage_2012_c=data_2012.fincome1_adj[data_2012["typ_hk"]=='城镇'].dropna().tolist()
wage_2014_c=data_2014.fincome1[data_2014["typ_hk"]=='城镇'].dropna().tolist()
wage_2016_c=data_2016.fincome1[data_2016["typ_hk"]=='城镇'].dropna().tolist()
wage_2018_c=data_2018.fincome1[data_2018["typ_hk"]=='城镇'].dropna().tolist()
'''wage_2010_c=deleteElem(wage_2010_c,-8)
wage_2012_c=deleteElem(wage_2012_c,-8)
wage_2014_c=deleteElem(wage_2014_c,-8)
wage_2016_c=deleteElem(wage_2016_c,-8)
wage_2018_c=deleteElem(wage_2018_c,-8)'''

#人均收入
wage_per_2012_c=data_2012.fincome1_per_adj[data_2012["typ_hk"]=='城镇'].dropna().tolist()
wage_per_2014_c=data_2014.fincome1_per[data_2014["typ_hk"]=='城镇'].dropna().tolist()
wage_per_2016_c=data_2016.fincome1_per[data_2016["typ_hk"]=='城镇'].dropna().tolist()
wage_per_2018_c=data_2018.fincome1_per[data_2018["typ_hk"]=='城镇'].dropna().tolist()
'''wage_per_2012_c=deleteElem(wage_per_2012_c,-8)
wage_per_2014_c=deleteElem(wage_per_2014_c,-8)
wage_per_2016_c=deleteElem(wage_per_2016_c,-8)
wage_per_2018_c=deleteElem(wage_per_2018_c,-8)'''


ind=np.arange(0,15,3)
width=0.5
color=['red','blue','green','red','blue','green']
x1=[np.mean(wage_2010_v),np.mean(wage_2012_v),np.mean(wage_2014_v),np.mean(wage_2016_v),np.mean(wage_2018_v)]
x2=[np.mean(wage_2010_c),np.mean(wage_2012_c),np.mean(wage_2014_c),np.mean(wage_2016_c),np.mean(wage_2018_c)]

plt.bar(ind,x1,width,align='edge',label='农村')
plt.bar(ind+width,x2,width,align='edge',label='城市')

plt.xticks(ind, ('2010', '2012', '2014', '2016', '2018'))
plt.legend()
plt.title("城乡家庭总收入对比")
plt.savefig("../图表/城乡家庭收入对比.png")
plt.show()


ind=np.arange(0,12,3)
width=0.5
color=['red','blue','green','red','blue','green']
x1=[np.mean(wage_per_2012_v),np.mean(wage_per_2014_v),np.mean(wage_per_2016_v),np.mean(wage_per_2018_v)]
x2=[np.mean(wage_per_2012_c),np.mean(wage_per_2014_c),np.mean(wage_per_2016_c),np.mean(wage_per_2018_c)]

plt.bar(ind,x1,width,align='edge',label='农村')
plt.bar(ind+width,x2,width,align='edge',label='城市')

plt.xticks(ind, ('2012', '2014', '2016', '2018'))
plt.legend()
plt.title("城乡家庭人均收入对比")
plt.savefig("../图表/城乡家庭人均收入对比.png")
plt.show()


#支出
#农村支出
out_2010_v=data_2010.fh601[data_2010["typ_hk"]=='乡村'].dropna().tolist()
out_2012_v=data_2012.expense[data_2012["typ_hk"]=='乡村'].dropna().tolist()
out_2014_v=data_2014.expense[data_2014["typ_hk"]=='乡村'].dropna().tolist()
out_2016_v=data_2016.expense[data_2016["typ_hk"]=='乡村'].dropna().tolist()
out_2018_v=data_2018.fexp[data_2018["typ_hk"]=='乡村'].dropna().tolist()
'''out_2010_v=deleteElem(out_2010_v,-8)
out_2012_v=deleteElem(out_2012_v,-8)
out_2014_v=deleteElem(out_2014_v,-8)
out_2016_v=deleteElem(out_2016_v,-8)
out_2018_v=deleteElem(out_2018_v,-8)'''
out_2010_v = list(map(int, pd.Series(out_2010_v).dropna()))
out_2012_v = list(map(int, pd.Series(out_2012_v).dropna()))
out_2014_v = list(map(int, pd.Series(out_2014_v).dropna()))
out_2016_v = list(map(int, pd.Series(out_2016_v).dropna()))
out_2018_v = list(map(int, pd.Series(out_2018_v).dropna()))

#人均支出

# wage_per_2012_v=data_2012.fincome1_per_adj[data_2012["typ_hk"]=='乡村'].dropna().tolist()
# wage_per_2014_v=data_2014.fincome1_per[data_2014["typ_hk"]=='乡村'].dropna().tolist()
# wage_per_2016_v=data_2016.fincome1_per[data_2016["typ_hk"]=='乡村'].dropna().tolist()
# wage_per_2018_v=data_2018.fincome1_per[data_2018["typ_hk"]=='乡村'].dropna().tolist()
# wage_per_2012_v=deleteElem(wage_per_2012_v,-8)
# wage_per_2014_v=deleteElem(wage_per_2014_v,-8)
# wage_per_2016_v=deleteElem(wage_per_2016_v,-8)
# wage_per_2018_v=deleteElem(wage_per_2018_v,-8)

#城市
out_2010_c=data_2010.fh601[data_2010["typ_hk"]=='城镇'].dropna().tolist()
out_2012_c=data_2012.expense[data_2012["typ_hk"]=='城镇'].dropna().tolist()
out_2014_c=data_2014.expense[data_2014["typ_hk"]=='城镇'].dropna().tolist()
out_2016_c=data_2016.expense[data_2016["typ_hk"]=='城镇'].dropna().tolist()
out_2018_c=data_2018.fexp[data_2018["typ_hk"]=='城镇'].dropna().tolist()
'''out_2010_c=deleteElem(out_2010_c,-8)
out_2012_c=deleteElem(out_2012_c,-8)
out_2014_c=deleteElem(out_2014_c,-8)
out_2016_c=deleteElem(out_2016_c,-8)
out_2018_c=deleteElem(out_2018_c,-8)'''
out_2010_c = list(map(int, pd.Series(out_2010_c).dropna()))
out_2012_c = list(map(int, pd.Series(out_2012_c).dropna()))
out_2014_c = list(map(int, pd.Series(out_2014_c).dropna()))
out_2016_c = list(map(int, pd.Series(out_2016_c).dropna()))
out_2018_c = list(map(int, pd.Series(out_2018_c).dropna()))
#人均收入
# wage_per_2012_c=data_2012.fincome1_per_adj[data_2012["typ_hk"]=='城镇'].dropna().tolist()
# wage_per_2014_c=data_2014.fincome1_per[data_2014["typ_hk"]=='城镇'].dropna().tolist()
# wage_per_2016_c=data_2016.fincome1_per[data_2016["typ_hk"]=='城镇'].dropna().tolist()
# wage_per_2018_c=data_2018.fincome1_per[data_2018["typ_hk"]=='城镇'].dropna().tolist()
# wage_per_2012_c=deleteElem(wage_per_2012_c,-8)
# wage_per_2014_c=deleteElem(wage_per_2014_c,-8)
# wage_per_2016_c=deleteElem(wage_per_2016_c,-8)
# wage_per_2018_c=deleteElem(wage_per_2018_c,-8)


ind=np.arange(0,15,3)
width=0.5
color=['red','blue','green','red','blue','green']
x1=[np.mean(out_2010_v),np.mean(out_2012_v),np.mean(out_2014_v),np.mean(out_2016_v),np.mean(out_2018_v)]
x2=[np.mean(out_2010_c),np.mean(out_2012_c),np.mean(out_2014_c),np.mean(out_2016_c),np.mean(out_2018_c)]

plt.bar(ind,x1,width,align='edge',label='农村')
plt.bar(ind+width,x2,width,align='edge',label='城市')

plt.xticks(ind, ('2010', '2012', '2014', '2016', '2018'))
plt.legend()
plt.title("城乡家庭总支出对比")
plt.savefig("../图表/城乡家庭总支出对比.png")
plt.show()


#x相关性检验
income_2018=pd.read_excel("../数据/家庭收支/家庭收支2018.xlsx").dropna()
fincom1_2018_v=income_2018["fincome1"].tolist()
N_S=income_2018["N_S"].tolist()
E_C_W_EW=income_2018["E_C_W_EW"].tolist()


print(scipy.stats.spearmanr(fincom1_2018_v, N_S))
print(scipy.stats.spearmanr(fincom1_2018_v, E_C_W_EW))


#方差检验
income_E=income_2018.fincome1[income_2018["E_C_W_EW"] == "E"].tolist()
income_C=income_2018.fincome1[income_2018["E_C_W_EW"] == "C"].tolist()
income_W=income_2018.fincome1[income_2018["E_C_W_EW"] == "W"].tolist()
income_S=income_2018.fincome1[income_2018["N_S"] == "S"].tolist()
income_N=income_2018.fincome1[income_2018["N_S"] == "N"].tolist()

# voter_frame = pd.DataFrame({"E":income_E,"C":income_C,"W":income_W,"S":income_S,"N":income_N})
voter_frame = [income_E, income_C, income_W, income_N, income_S]
model = ols('fincome1 ~ C(N_S)+C(E_C_W_EW)',
            data=income_2018).fit()

anova_result = sm.stats.anova_lm(model, typ=2)

print(anova_result)