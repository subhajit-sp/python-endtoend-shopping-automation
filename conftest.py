import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver_init(request):
    driver = webdriver.Chrome()
    from selenium.webdriver.support.wait import WebDriverWait
    implicitly_wait = WebDriverWait(driver, 5)
    yield driver
    driver.close()