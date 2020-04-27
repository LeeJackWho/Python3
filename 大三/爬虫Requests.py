import requests
# r=requests.get("https://www.baidu.com")
# print(r.status_code)
# type(r)
# r.headers
# r.encoding=r.apparent_encoding
# r.text

# def getHTMLText(url):
#     try:
#         r=requests.get(url,timeout=30)
#         r.raise_for_status()
#         r.encoding=r.apparent_encoding
#         return  r.text
#     except:
#         return "产生异常"
# if __name__=="__main__":
#     url="http://www.baidu.com"
#     print(getHTMLText(url))

# r=requests.get("https://item.jd.com/5706773.html")
# r.status_code
# r.encoding
# r.text[:1000]
# url="https://item.jd.com/5706773.html"
# try:
#     r=requests.get(url,timeout=30)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     r.text[:1000]
#     print(r.text)
# except:
#      print("网络访问异常")

# 搜索全代码
# keyword="Python"
# try:
#     kv={'wd':keyword}
#     r=requests.get("http://www.baidu.com",params=kv)
#     print(r.request.url)
#     r.raise_for_status()
#     print(len(r.text))
# except:
#     print("爬取失败")

# 爬取图片
path="E://Python//C1//dy.jpg"
url="https://imgoss.douyucdn.cn/bj/yuba/default/2019/09/30/201909300117293264405431844.jpg"
r=requests.get(url)
r.status_code
with open(path,'wb')as f:
    f.write(r.content)
    f.close()