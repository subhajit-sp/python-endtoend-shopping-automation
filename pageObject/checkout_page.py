from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.country_name = (By.ID, 'country')
        self.visibility_element = (By.XPATH, "//div[@class = 'suggestions']/ul/li")
        self.checkbox_button = (By.ID, 'checkbox2')
        self.submit_button = (By.XPATH, "//input[@class = 'btn btn-success btn-lg' and @type = 'submit']")
        self.msg_window = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def checkout(self, country_name, user_input):
        """this is the final page, add country and complete purchase"""
        self.driver.find_element(*self.country_name).send_keys(user_input)
        countries = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.visibility_element))
        for country in countries:
            if country.text == country_name:
                country.click()
                break
        action = ActionChains(self.driver)
        action.click(self.driver.find_element(*self.checkbox_button)).perform()
        self.driver.find_element(*self.submit_button).click()
        print(self.driver.find_element(*self.msg_window).text)
