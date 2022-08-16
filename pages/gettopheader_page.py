from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

# ACCOUNT = (By.CSS_SELECTOR, "i.icon-user")
ACCOUNT = (By.CSS_SELECTOR, 'a[href="https://gettop.us/my-account/"]')
LOGIN_PAGE = (By.CSS_SELECTOR, "h3")
HAMBURGER_MENU = (By. CSS_SELECTOR, ".icon-menu")
HAMBURGER_MENU_MOBILE = (By.XPATH,"//div[@class='flex-col show-for-medium flex-left']/ul/li/a" )



class GettopheaderPage(Page):

    def open_gettopheader(self):
        self.open_page() #f'https://gettop.us/'

    def click_on_account_icon(self):
        self.driver.find_element(*ACCOUNT).click()

    def verify_login_form_opens(self, expected_result):
        self.wait_for_element_appear(*LOGIN_PAGE)
        actual_result = self.find_element(*LOGIN_PAGE).text
        assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'

    def click_over_hamburger_menu(self):
        self.wait_for_element_click(*HAMBURGER_MENU)

    def click_login_option(self):
        self.click(*ACCOUNT)

