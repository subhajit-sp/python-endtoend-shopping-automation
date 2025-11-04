from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, 'name')
        self.email = (By.NAME, 'email')
        self.password = (By.ID, 'exampleInputPassword1')
        self.submitbutton = (By.XPATH, "//input[@type = 'submit' and @class = 'btn btn-success']")
        self.shopbutton = (By.XPATH, "//a[@class = 'nav-link' and text() = 'Shop']")



    def login(self, uname, email, password):
        """Fill login form and navigate to shop page"""
        self.driver.find_element(*self.username).send_keys(uname)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.submitbutton).click()
        self.driver.find_element(*self.shopbutton).click()
