from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

ACCOUNT = (By.CSS_SELECTOR, "i.icon-user")
LOGIN_PAGE = (By.CSS_SELECTOR, "h3")

class GettopheaderPage(Page):

    def open_gettopheader(self):
        self.open_page() #f'https://gettop.us/'

    def click_on_account_icon(self):
        self.driver.find_element(*ACCOUNT).click()

    def verify_login_form_opens(self, expected_result):
        self.wait_for_element_appear(*LOGIN_PAGE)
        actual_result = self.find_element(*LOGIN_PAGE).text
        assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'

