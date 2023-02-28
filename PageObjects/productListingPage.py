from selenium.webdriver.common.by import By

class ProductListingPage:
    header_product_xpath = "//div[@id='header_container']//span[@class='title']"
    first_product_name_class = "inventory_item_name"
    button_burger_menu_id = "react-burger-menu-btn"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def getHeaderTitle(self):
        return self.driver.find_element(By.XPATH,self.header_product_xpath).text

    def getFirstProductName(self):
        return self.driver.find_element(By.CLASS_NAME, self.first_product_name_class).text

    def clickBurgerMenu(self):
        self.driver.find_element(By.ID, self.button_burger_menu_id).click()
    
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
