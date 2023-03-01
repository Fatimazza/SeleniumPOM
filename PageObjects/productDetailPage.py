from selenium.webdriver.common.by import By

class ProductDetailPage:
    text_product_name_css = "div.inventory_details_name"
    text_product_desc_css = "div.inventory_details_desc"
    text_product_price_css = "div.inventory_details_price"

    def __init__(self, driver):
        self.driver = driver

    def getProductName(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_product_name_css).text

    def getProductDesc(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_product_desc_css).text

    def getProductPrice(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_product_price_css).text