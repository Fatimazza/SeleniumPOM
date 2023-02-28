import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.loginPage import LoginPage
from PageObjects.productListingPage import ProductListingPage

class SaucedemoLogin(unittest.TestCase):
    baseUrl = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.baseUrl)

    def test_a_success_login_standard_user(self):
        loginpage = LoginPage(self.browser)
        loginpage.setUsername(self.username)
        loginpage.setPassword(self.password)
        loginpage.clickLogin()
        # assertion
        productListingPage = ProductListingPage(self.browser)
        header_title = productListingPage.getHeaderTitle()
        self.assertEqual(header_title, "PRODUCTS")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    # run all test
    unittest.main()