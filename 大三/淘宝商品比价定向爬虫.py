import requests
import re


# 获得页面函数
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "failed\n"


# 对每个获得页面进行解析
# 第一个变量结果的列表类型
# 第二个变量相关的html信息
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  # eval的函数将字符串转为数字
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


# 输出商品信息
def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


# 主函数
def main():
    goods = '书包'
    depth = 2  # 改段代码是演示用的，depth不能太大，淘宝本是不允许爬取搜索页面的
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodList(infoList)

main()
