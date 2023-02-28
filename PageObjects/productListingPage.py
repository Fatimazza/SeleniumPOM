from selenium.webdriver.common.by import By

class ProductListingPage:
    header_product_xpath = "//div[@id='header_container']//span[@class='title']"
    first_product_name_class = "inventory_item_name"

    def __init__(self, driver):
        self.driver = driver

    def getHeaderTitle(self):
        return self.driver.find_element(By.XPATH,self.header_product_xpath).text

    def getFirstProductName(self):
        return self.driver.find_element(By.CLASS_NAME, self.first_product_name_class).text
