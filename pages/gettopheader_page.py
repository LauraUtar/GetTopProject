from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

ACCOUNT = (By.CSS_SELECTOR, "i.icon-user")
LOGIN_PAGE = (By.CSS_SELECTOR, "#login-form-popup")

class GettopheaderPage(Page):

    def open_gettopheader(self):
        self.open_page(f'https://gettop.us/')

    def click(self, *ACCOUNT):
        self.driver.find_element(*ACCOUNT).click()

    def verify_login_form_opens(context):
        context.driver.wait.until(EC.visibility_of_element_located(*LOGIN_PAGE))

    # def verify_signin_popup_shown(self):
    #     return self.wait.until(EC.visibility_of_element_located(SIGN_IN_POPUP_BTN), message='SignIn btn not visable')
    #
    # def verify_signin_popup_btn_is_clickable(self):
    #     signin_popup_btn = self.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN), message='SignIn btn not clickable')
    #     signin_popup_btn.click()
    #
    # def verify_signin_popup_disappears(self, *SIGN_IN_POPUP_BTN):
    #     self.wait.until(EC.invisibility_of_element(SIGN_IN_POPUP_BTN))
    #
    #

