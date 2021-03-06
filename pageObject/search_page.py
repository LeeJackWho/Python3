from basePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    # 搜索框元素
    input_id = (By.ID, 'kw')
    # 百度一下按钮
    click_id = (By.ID, 'su')

    # 对搜素框进行内容输入
    def input_text(self, input_text):
        self.locator(self.input_id).send_keys(input_text)

    # 点击查询按钮实现搜索
    def click_element(self):
        self.locator(self.click_id).click()

    def check(self, url, input_text):
        self.visit(url)
        self.input_text(input_text)
        self.click_element()


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    driver = webdriver.Chrome()
    sp = SearchPage(driver)
    # 进行调试
    sp.check(url, '666')
    # sp.visit(url)
    # sp.input_text('xuzhu')
    # sp.click_element()
