import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class SaucedemoProduct(unittest.TestCase):
    baseUrl = "https://www.saucedemo.com/"

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.baseUrl)
        time.sleep(5)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    # run all test
    unittest.main()