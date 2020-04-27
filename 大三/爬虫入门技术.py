from bs4 import BeautifulSoup
import requests
import os

book_url = 'html://www.biquw.com/book'
content = requests.get(book_url).text
soup = BeautifulSoup(content,'lxml')
#多个div使用字典id为htmlContent进行定位
book_content = soup.find('div',{'id':'htmlContent'}).text

#自动创建保存小说文件的文件夹
if not os.path.exists('./小说/'):
    os.makedirs('./小说/')

#将筛选好的数据保存到文本中 文件处理
with open('./小说' + book_data.text + 'txt','w',encoding='utf-8')as f:
    #写入数据
    f.write(book_content)

