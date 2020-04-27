# import os
# #创建文件夹
# os.mkdir("张三")
# os.mkdir("./data/张三")#当前路径下data文件夹必须存在
# #获取当前目录
# os.getcwd()
# #改变默认目录
# os.chdir("../")
# #获取目录列表
# os.listdir("./")
# #删除文件夹
# os.rmdir("张三")

#使用xlwt读写Excel文件

#写csv文件
import csv
with open("test.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    writer.writerow(["index","a_name","b_name"])
    #写入多行用writerows
    writer.writerows([0,1,3],[1,2,3],[2,3,4])

#读CSV文件
import csv
with open("test.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    #这里不需要readlines
    for line in reader:
        print(line)

#运用pandas包操作CSV文件
#写入csv文件，任意的多组列表
import pandas as pd
a=[1,2,3]
b=[4,5,6]
dataframe=pd.DataFrame({'a_name':a,'b_name':b})
#将Dataframe存储为csv，index表示是否显示行名，default=true
dataframe.to_csv("test.csv",index=False)
#读csv文件
data=pd.read_csv('test.csv')