# 导包
from selenium import webdriver
from time import sleep

# 去掉黄条
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# 不启动浏览器即无头模式
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)
# 访问url
driver.get('http://localhost:9000/jenkins/login?from=%2Fjenkins%2F')

# 输入用户名
driver.find_element_by_id('j_username').send_keys('aaa')
# 输入密码
driver.find_element_by_name('j_password').send_keys('aaaaa')
# 点击登录
driver.find_element_by_xpath('/html/body/div/div/form/div[4]/input').click()
# 等待
sleep(3)
# 关闭驱动
driver.quit()
