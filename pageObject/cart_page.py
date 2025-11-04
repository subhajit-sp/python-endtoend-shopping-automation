from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.items_in_cart = (By.XPATH, "//h5[@class = 'media-heading' ]")
        self.checkout_button = (By.XPATH, "//button[@class = 'btn btn-success']")


    def clicktocheckout(self):
        """verify the cart page and click to the checkout button"""
        if len(self.driver.find_elements(*self.items_in_cart)) > 0:
            self.driver.find_element(*self.checkout_button).click()
        else:
            raise Exception("Cart is empty")


