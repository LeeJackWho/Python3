
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 淘宝对搜索进行了限制，只有登录账号之后才能进行搜索，就算selenium模拟用户登录也需要进行滑块验证
# 可以通过保存cookie绕过登录限制（参考：https://blog.csdn.net/a564126786/article/details/87908926），但比较麻烦，所以爬取京东信息
# chromedriver的绝对路径
driver_path = r'E:\Google\Chrome\Application\chromedriver.exe'

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


with open("京东手机信息.txt",'w') as f:
    for shop in mylist:
        f.write(str(shop) + "\n")












