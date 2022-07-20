from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep


ACCOUNT = (By.CSS_SELECTOR, "i.icon-user")
LOGIN_PAGE = (By.CSS_SELECTOR, "h3")


@given("Open GetTop")
def open_gettop(context):
    # context.driver.get(f'https://gettop.us/')
    context.app.gettopheader_page.open_gettopheader()

@when("Click on Account icon")
def click_on_account_icon(context):
    context.app.gettopheader_page.click_on_account_icon()

@then("Verify login form opens")
def verify_login_form_opens(context):
    context.app.gettopheader_page.verify_login_form_opens("LOGIN")