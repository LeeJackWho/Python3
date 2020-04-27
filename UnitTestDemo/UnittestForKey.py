# 导包
import unittest
from time import sleep
from CeMa.KeyWordsDemo import TestKeyWords
# from ddt import ddt, data, unpack
#
#
# @ddt
class TestForKey(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        self.tk = TestKeyWords('http://localhost:9000/jenkins/login?from=%2Fjenkins%2F', 'chrome')

    # 后置条件
    def tearDown(self) -> None:
        self.tk.quit_browser()

    # 测试用例1
    def test_1(self):
        self.tk.input_text('id', 'j_username', 'aaa')
        self.tk.input_text('name', 'j_password', 'Aaaaa')
        self.tk.click_element('xpath', '/html/body/div/div/form/div[4]/input')
        sleep(3)

    # 测试用例2
    # *表示基于元组的形式进行处理，**表示字典基于键值对形式去获取
    # @data(['id', 'aaa'], ['name', 'AAaaa'])
    # @unpack
    #     # def test_2(self, locator, input_value):
    #     #     self.tk.input_text(locator, 'j_username', input_value)
    #     #     self.tk.input_text('name', 'j_password', 'aaaaa')
    #     #     self.tk.click_element('xpath', '/html/body/div/div/form/div[4]/input')
    #     #     sleep(3)


if __name__ == '__main__':
    unittest.main()