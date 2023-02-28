from selenium.webdriver.common.by import By

class ProductListingPage:
    header_product_xpath = "//div[@id='header_container']//span[@class='title']"

    def __init__(self, driver):
        self.driver = driver

    def getHeaderTitle(self):
        return self.driver.find_element(By.XPATH,self.header_product_xpath).text
