from selenium.webdriver.common.by import By


class ShoppingPage:
    def __init__(self, driver):
        self.driver = driver
        self.finditems = (By.XPATH, "//h4[@class = 'card-title']")
        self.addtocard_button = (By.XPATH, ".//ancestor::div[@class = 'card h-100']//button")
        self.gotocart_button = (By.XPATH, "//a[@class = 'nav-link btn btn-primary']")

    def select_item(self, pname):
        """Select item and add it to cart. process to cart page"""
        item_list = self.driver.find_elements(*self.finditems)
        item_found = False
        for item in item_list:
            if item.text == pname:
                item.find_element(*self.addtocard_button).click()
                item_found = True
                break
        assert item_found, "Item not found"
        self.driver.find_element(*self.gotocart_button).click()

