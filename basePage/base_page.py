# 这是基本类
from selenium import webdriver


class BasePage(object):

    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def locator(self, locator):
        return self.driver.find_element(*locator)

    # 关闭
    def quit_browser(self):
        self.driver.quit()

    # 访问url
    def visit(self, url):
        self.driver.get(url)
