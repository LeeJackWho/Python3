"""
2018年对比2015、2016、2017年的财务变化
"""

import  pandas as pd
import numpy as np
df={}
diff={}
for i in range(8,4,-1):
    file_str="./胡润富豪榜/胡润富豪榜201"+str(i)+".xlsx"
    df[2010 + i] =pd.read_excel(file_str).set_index("姓名")
    if i==8:
        df_diff=df[2018]['财富 (人民币)']
    if i<8:
        diff[2010+i]=(df[2018]['财富 (人民币)'].str[:-2].astype(int)-df[2010+i]['财富 (人民币)'].str[:-2].astype(int))  #str[:-2] 财富只取数值
        # diff[2010+i]=diff[2010+i].dropna()
        diff[2010+i]=diff[2010+i].reindex(index=df[2018].index)
total=pd.DataFrame({2018:df_diff,2017:diff[2017],2016:diff[2016],2015:diff[2015]})
total.to_csv("./胡润富豪榜/富豪榜各年的差值.csv")

#求平均年龄
# ages=[]
# for i in range(2015,2019):
#     age=df[i]["年龄"].astype(str)
#     print(age)
#     abc=age.str.replace("/","0")
#     bcd=abc.str.split("、")
#     print(bcd)
#     for a in bcd.values:
#         for b in a:
#             if b!="0":
#                 ages.append(int(b))
# print(ages)