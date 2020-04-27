import pandas as pd

from selenium import webdriver

# chromedriver的绝对路径
driver_path = r'D:\chromedriver_win32\chromedriver.exe'

# 初始化一个driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)
# 请求网页
driver.get("http://quote.eastmoney.com/")


text_list = []
# 里面存储的就是以下数据了
# 最新：15.31 均价：15.26
# 涨幅：1.66% 涨跌：0.25
# 总手：232.8万手 金额：35.53亿
# 换手：4.28% 量比：1.91
# 最高：15.52 最低：14.89
# 今开：15.09 昨收：15.06
# 涨停：16.57 跌停：13.55
# 外盘：129.3万 内盘：103.5万


for i in range(1,9):
    line = driver.find_element_by_xpath("/html/body/div[13]/div[2]/div[2]/div[1]/div[4]/table/tbody/tr["+str(i)+"]")
    text_list.append(line.text)

driver.close()

all_data = []
for re in text_list:
    lines = re.split(" ")
    all_data.append(lines[0].split("：")[1])
    all_data.append(lines[1].split("：")[1])

tao_list = []
tao_list.append(all_data)
list_Name = ['最新','均价','涨幅','涨跌','总手','金额','换手','量比','最高','最低','今开','昨收','涨停','跌停','外盘','内盘']
gupiao = pd.DataFrame(columns=list_Name,data=tao_list)
gupiao.to_csv('gupiao.csv')












