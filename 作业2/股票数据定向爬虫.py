# -*- coding:utf-8 -*-
import requests
from selenium import webdriver
import csv
#定义爬取上交所所有股票信息函数
def getSJPage(i):
    url = "http://80.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124007307516034361683_1570776924885&pn=" + str(i) + "&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1570776925172"
    r = requests.get(url)
    #通过split分割获取的信息[1]表示后面的部分，[0]表示前面的部分
    resp = r.text.split(':[')[1].split(']}')[0].split('},')
    return resp
#定义爬取深交所所有股票信息函数
def getSZPage(i):
    url="http://85.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112403711882297682425_1570869660976&pn="+ str(i) +"&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1570869661005"
    r=requests.get(url)
    resp = r.text.split(':[')[1].split(']}')[0].split('},')
    return resp
#f2最新价 f3涨跌幅 f4涨跌额 f5成交量(手) f6成交额 f7振幅 f8换手率 f9市盈率(动态) f10量比 f12代码 f14名称 f15最高 f16最低 f17今开 f18昨收 f23市净率
#定义第一行数据属性行的数组
stock = ['','最新价','涨跌幅','涨跌额','成交量(手)','成交额','振幅','换手率','市盈率(动态)','量比','','代码','','名称','最高','最低','今开','昨收','','','','市净率']
#保存上交所数据
out = open('上交所股票.csv','w',newline='')
csv_write = csv.writer(out,dialect='excel')
csv_write.writerow(stock)
out.close()
f=open('上交所股票.csv','a')
for i in range(1,80):
    resp = getSJPage(i)
    for item in resp:
        f.write(item + '\n')
f.flush()
f.close()
#保存深交所数据
out = open('深交所股票.csv','w',newline='')
csv_write = csv.writer(out,dialect='excel')
csv_write.writerow(stock)
out.close()
f=open('深交所股票.csv','a')
for i in range(1,112):
    resp = getSZPage(i)
    for item in resp:
        f.write(item + '\n')
f.flush()
f.close()

#选取一条你感兴趣的股票，从某个股票平台打开该股票的页面，获取时间、股价、涨跌幅等常用信息，输出在屏幕
#chromedriver的绝对路径
driver_path=r'E:\Google\Chrome\Application\chromedriver.exe'
# 初始化一个driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)
# 请求网页
driver.get("http://quote.eastmoney.com/sh600778.html")
infoList = []
for trs in range(1,9):
    tr = driver.find_element_by_xpath("/html/body/div[13]/div[2]/div[2]/div[1]/div[4]/table/tbody/tr["+str(trs)+"]")
    infoList.append(tr.text)
with open("个股信息.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    #写入csv
    writer.writerow(infoList)
    csvfile.close()