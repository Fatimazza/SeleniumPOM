import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class SaucedemoLogin(unittest.TestCase):
    baseUrl = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.baseUrl)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    # run all test
    unittest.main()