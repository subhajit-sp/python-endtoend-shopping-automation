from pageObject.login_page import LoginPage
from pageObject.shop_page import ShoppingPage
from pageObject.cart_page import CartPage
from pageObject.checkout_page import CheckoutPage
from test_data import TestData

def test_purchase(driver_init):
    driver = driver_init
    driver.maximize_window()
    driver.get(TestData.BASE_URL)

    #login page and go to shopping page
    login = LoginPage(driver)
    login.login(TestData.USER_NAME, TestData.USER_EMAIL, TestData.USER_PASSWORD)
    assert driver.title == TestData.TITLE, "Incorrect page loaded"
    print("Successfully Logged in")

    #from shopping page and select item and add to card function
    shop = ShoppingPage(driver)
    shop.select_item(TestData.PRODUCT_NAME)
    print("Item added to cart")

    #verify the cart page and select checkout
    cartpage = CartPage(driver)
    cartpage.clicktocheckout()

    #Checkout page, select country and click purchase button
    chkpage = CheckoutPage(driver)
    chkpage.checkout(TestData.COUNTRY, TestData.USER_INPUT)

    driver.get_screenshot_as_file('screenshot-endtoend.png')
    #time.sleep(2)