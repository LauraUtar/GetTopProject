from behave import given, then, when
from selenium.webdriver.common.by import By
from time import sleep


@given("Open GetTop browse page")
def open_gettop_browse(context):
    context.app.gettopbrowser_page.open_gettopbrowser()

@when("Click on {search_word}")
def click_on_search_word(context, search_word):
    context.app.gettopbrowser_page.open_gettopbrowser()

@then("Verify search results are shown for {expected_result}")
def verify_search_results_text(context, expected_result):
    context.app.gettopbrowser_page.verify_search_results_text
