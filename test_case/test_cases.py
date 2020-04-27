import unittest
from selenium import webdriver
from pageObject.search_page import SearchPage
from time import sleep


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        driver = webdriver.Chrome()
        self.sp = SearchPage(driver)

    def tearDown(self) -> None:
        self.sp.quit_browser()

        def test_1(self, url, input_text):
            self.sp.check(url, input_text)
            sleep(3)
if __name__ == '__main__':
    unittest.main()