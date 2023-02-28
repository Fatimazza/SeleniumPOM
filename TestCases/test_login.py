import time
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
        time.sleep(5)

    def test_a_success_login_standard_user(self):
        loginPage = LoginPage(self.browser)
        loginPage.setUsername(self.username)
        loginPage.setPassword(self.password)
        loginPage.clickLogin()
        time.sleep(5)
        # assertion
        productListingPage = ProductListingPage(self.browser)
        header_title = productListingPage.getHeaderTitle()
        self.assertEqual(header_title.casefold(), "PRODUCTS".casefold())
        first_product_name = productListingPage.getFirstProductName()
        self.assertEqual(first_product_name, "Sauce Labs Backpack")
    
    def test_b_success_logout(self):
        # step to login
        loginPage = LoginPage(self.browser)
        loginPage.setUsername(self.username)
        loginPage.setPassword(self.password)
        loginPage.clickLogin()
        time.sleep(5)
        # step to logout
        productListingPage = ProductListingPage(self.browser)
        productListingPage.clickBurgerMenu()
        time.sleep(3)
        productListingPage.clickLogout()
        time.sleep(5)
        # assertion
        login_text = loginPage.getLoginButton()
        self.assertEquals(login_text.casefold(), "LOGIN".casefold())

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    # run all test
    unittest.main()