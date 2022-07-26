from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep


# ACCOUNT = (By.CSS_SELECTOR, "i.icon-user")
ACCOUNT = (By.CSS_SELECTOR, 'a[href="https://gettop.us/my-account/"]')
LOGIN_PAGE = (By.CSS_SELECTOR, ".account-login-inner h3")


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


@when("Click over hamburger menu")
def click_over_hamburger_menu(context):
    context.app.gettopheader_page.click_over_hamburger_menu()


@when("Click login option")
def click_login_option(context):
    context.app.gettopheader_page.click_login_option()

