from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class GettopbrowserPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, "ul.product-categories li")


    def open_gettopbrowser(self):
        self.open_page() #f'https://gettop.us/'

    def click_on_search_word(self):
        self.driver.find_element(*SEARCH_RESULT).click()

    def verify_search_results_text(self, expected_result):
        self.wait_for_element_appear(*SEARCH_RESULT)
        actual_result = self.find_element(*SEARCH_RESULT).text
        assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'

