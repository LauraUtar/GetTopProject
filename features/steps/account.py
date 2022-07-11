from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep


ACCOUNT = (By.CSS_SELECTOR, "i.icon-user")
LOGIN_PAGE = (By.CSS_SELECTOR, "#login-form-popup")


# ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
# PRODUCT_NAME = (By.ID, 'productTitle')
# COLOR_OPTIONS = (By.CSS_SELECTOR, "#inline-twister-expander-content-color_name li[class*='desktop']")
# COLOR_NAME = (By.ID, 'inline-twister-expander-content-color_name')

@given("Open GetTop")
def open_gettop(context):
    # context.driver.get(f'https://gettop.us/')
    context.app.gettopheader_page.open_gettopheader()

@when("Click on Account icon")
def click_on_account_icon(context):
    context.driver.find_element(*ACCOUNT).click()

@then("Verify login form opens")
def verify_login_form_opens(context):
    context.driver.wait.until(EC.visibility_of_element_located(ACCOUNT))



