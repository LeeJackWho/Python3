# 导入四个库
import requests
from bs4 import BeautifulSoup
import traceback
import re


# 获得url页面
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        # 返回空字符串
        return ""

# 获得股票信息列表
# 有两个参数
# 第一个是列表保存的列表类型
# 第二个参数是获取股票url
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    # 股票名称和代号在网页源代码的a标签的href属性上
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue

# 获得每一条个股的股票信息并且存到数据结构
# 三个参数
# 第一个保存所有股票的信息列表
# 第二个是获取股票url
# 第三个是将来保存信息的文件路径
def getStockInfo(stockList, stockURL, fpath):
    for stock in stockList:
        url = stockURL + stock + ".html"  # 个股的详细查询页面
        html = getHTMLText(url)
        try:
            if html == "":  # 异常判断
                continue
            # 定义字典存储返回的个股信息
            infoDict = {}
            # 解析网页类型
            soup = BeautifulSoup(html, 'html.parser')
            # 找到第一个class属性值为stock-bets的div标签
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

            if stockInfo == None:  # 异常判断
                continue
            # 找到第一个class属性为bets-name的a标签
            name = stockInfo.find('a', attrs={'class': 'bets-name'})
            # 得到股票名称
            infoDict.update({'股票名称': name.text.split()[0]})
            # 通过阅读页面源码，发现数据可用键值对的形式存储
            # 找到所有dt标签（数据键值对的键）
            keyList = stockInfo.find_all('dt')
            # 找到所有dd标签（数据键值对的值）
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            # 将新增数据添加到文件
            with open(fpath, 'a', encoding='utf-8')as f:
                f.write(str(infoDict) + '\n')
        except:
            # 打印异常信息，这样的做法是出现异常，异常信息可以打印出来，但是程序仍会接着进行
            traceback.print_exc()
            continue


# 主函数
def main():
    # 股票列表页面（可得到所有股票代号和名称）
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    # 个股详细查询页面（根据股票代号可查询）
    stock_info_url = 'https://gupiao.baidu.com/stock'
    # 保存爬取数据文件
    output_file = 'BaiduStockInfo.txt'
    # 股票列表
    stockList = []
    # 得到股票列表
    getStockList(stockList, stock_list_url)
    # 得到所有个股的详细信息，并保存在输出文件
    getStockInfo(stockList, stock_info_url, output_file)

main()
