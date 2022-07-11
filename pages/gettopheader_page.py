from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

ACCOUNT = (By.CSS_SELECTOR, "i.icon-user")
LOGIN_PAGE = (By.CSS_SELECTOR, "#login-form-popup")

class GettopheaderPage(Page):

    def open_gettopheader(self):
        self.open_page() #f'https://gettop.us/'

    def click(self, *ACCOUNT):
        self.driver.find_element(*ACCOUNT).click()

    def verify_login_form_opens(context):
        context.driver.wait.until(EC.visibility_of_element_located(*LOGIN_PAGE))


