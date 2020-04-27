import http
import json
from bs4 import BeautifulSoup

# 抓取天猫胸罩销售评论
def getRateDetail(itemId,currentPage):
    # Url最后的callback字段是用于天猫网站内部回调，和我们没关系，不过这个字段的值关系到返回数据的前缀，我们可以利用这个值截取返回数据
    url='https://rate.tmall.com/list_detail_rate.htm?itemId=' + str(itemId) + '&spuId=418357413&sellerId=765844183&order=3&currentPage=' + str(currentPage) + '&append=0......&callback=jsonp462'
    r = http.request('GET',url,headers = headers)
    # 返回数据时GB18030编码，所以要用这个编码格式进行解码
    c = r.data.decode('GB18030')
    # 下面的代码返回评论数据转换为JSON格式
    c = c.replace('jasonp1278(','')
    c = c.replace(')','')
    c = c.replace('false','"false"')
    c = c.replace('true','"true"')
    # 将JSON格式的评论数据转换成字典
    tmalljson = json.loads(c)
    return tmalljson

# 抓取胸罩商品列表
def getProductIdList():
    url = 'https://list.tmall.com/search_product.htm... ...'
    r = http.request('GET', url,headers = headers)
    c = r.data.decode('GB18030')
    soup = BeautifulSoup(c,'lxml')
    linkList = []
    idList = []
    # 用Beautiful Soup提取商品页面中所有的商品ID
    tags = soup.find_all(href=re.compile('detail.tmall.com/item.htm'))
    for tag in tags:
        linkList.append(tag['href'])
    linkList = list(set(linkList))
    for link in linkList:
        aList = link.split('&')
        # //detail.tmall.com/item.htm?id=562173686340
        # 将商品ID添加到列表中
        idList.append(aList[0].replace('//detail.tmall.com/item.htm?id=',''))
    return idList

# 通过getLastPage函数获得最大评论页数
def getLastPage(itemId):
    tmalljson = getRateDetail(itemId,1)
    return tmalljson['rateDetail']['paginator']['lastPage']

# 对商品ID进行迭代
while initial < len(productIdList):
    try:
        itemId = productIdList[initial]
        print('----------',itemId,'------------')
        maxnum = getLastPage(itemId)
        num = 1
        while num <= maxnum:
            try:
                # 抓取某个商品的某页评论数据
                tmalljson = getRateDetail(itemId, num)
                rateList = tmalljson['rateDetail']['rateList']
                n = 0
                while n < len(rateList):
                    # 颜色分类:H007浅蓝色加粉色;尺码:32/70A
                    colorSize = rateList[n]['auctionSku']
                    m = re.split('[:;]',colorSize)
                    rateContent = rateList[n]['rateContent']
                    color = m[1]
                    size = m[3]
                    dtime = rateList[n]['rateDate']
                    # 将抓取的数据保存

                    n += 1
                    print(color)
                print(num)
                num += 1
            except Exception as e:
                continue
        initial += 1
    except Exception as e:
        print(e)

# 用Pandas和Matplotlib分析对胸罩销售比例进行可视化分析
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
# 打开bra.sqlite数据库
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
# 查询t_sales表中所有的数据
sales = read_sql('select source,size1 from t_sales',engine)
# 对size1进行分组，并统计每一组的记录数
size1Count = sales.groupby('size1')['size1'].count()
print(size1Count)
# 计算总销售数量
size1Total = size1Count.sum()
print(size1Total)
print(type(size1Count))
# 将Series转换为DataFrame
size1 = size1Count.to_frame(name='销量')
print(size1)
# 格式化浮点数
options.display.float_format = '{:,.2f}%'.format
# 插入新的“比例”列
size1.insert(0,'比例', 100 * size1Count / size1Total)
print(size1)
# 将索引名改为“罩杯”
size1.index.names=['罩杯']
print(size1)

# 数据可视化
print(size1['销量'])
# 饼图要显示的文本
labels = ['A罩杯','B罩杯','C罩杯','D罩杯']
# 用饼图绘制销售比例
size1['销量'].plot(kind='pie',labels = labels, autopct='%.2f%%')
# 设置长宽相同
axis('equal')
legend()
show()