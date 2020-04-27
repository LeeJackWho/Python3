import csv

from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 你以为是淘宝的吗？不可能，根本进不去，用下京东的吧！！！！！
# chromedriver的绝对路径
driver_path = r'D:\chromedriver_win32\chromedriver.exe'

# 初始化一个driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)
# 请求网页
driver.get("https://www.jd.com/")

# 定位搜索框 输入 手机 搜索词 ， 然后模仿点击行为
mylist = []
searchbox = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div/div[2]/input").send_keys('手机')
searchbutton = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div/div[2]/button/i").click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[1]/a[2]/span"))
    )
finally:
    salenum = driver.find_element_by_xpath(
        "/html/body/div[6]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[1]/a[2]/span").click()

    time.sleep(3)

    # 执行以下行为的次数
    for i in range(2):

        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)

        time.sleep(3)


        for i in range(1,61):
            # "+str(i)+"
            try:
                shopname = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li["+str(i)+"]/div/div[7]/span/a")
                title = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li["+str(i)+"]/div/div[4]/a/em")
                price = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li["+str(i)+"]/div/div[3]/strong/i")
            except:
                continue
            mydic = {
                'shopname':shopname.text,
                'title':title.text,
                'price':price.text
            }
            mylist.append(mydic)

        driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div[1]/div/div[3]/div/span[1]/a[9]/em").click()
        time.sleep(3)

driver.close()

# with open("mytext.txt",'w') as fp:
#     for shop in mylist:
#         fp.write(str(shop) + "\n")

# write nested list of dict to csv
def nestedlist2csv(list, out_file):
    with open(out_file, 'w',encoding="gbk") as f:
        w = csv.writer(f)
        fieldnames=list[0].keys()  # solve the problem to automatically write the header
        w.writerow(fieldnames)
        for row in list:
            w.writerow(row.values())


nestedlist2csv(mylist,"test.csv")







