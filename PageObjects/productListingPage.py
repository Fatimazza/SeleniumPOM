from selenium.webdriver.common.by import By

class ProductListingPage:
    text_header_xpath = "//div[@id='header_container']//span[@class='title']"
    text_first_product_name_class = "inventory_item_name"
    text_third_product_name_xpath = "/html//div[@id='inventory_container']/div/div[@id='inventory_container']/div/div[3]/div[@class='inventory_item_description']/div[@class='inventory_item_label']/a[@href='#']/div[@class='inventory_item_name']"
    button_burger_menu_id = "react-burger-menu-btn"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def getHeaderTitle(self):
        return self.driver.find_element(By.XPATH,self.text_header_xpath).text

    def getFirstProductName(self):
        return self.driver.find_element(By.CLASS_NAME, self.text_first_product_name_class).text

    def getThirdProductName(self):
        return self.driver.find_element(By.XPATH, self.text_third_product_name_xpath).text

    def clickBurgerMenu(self):
        self.driver.find_element(By.ID, self.button_burger_menu_id).click()
    
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
