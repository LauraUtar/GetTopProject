from pages.gettopheader_page import GettopheaderPage
from pages.gettopbrowser_page import GettopbrowserPage
from pages.base_page import Page

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.gettopheader_page = GettopheaderPage(self.driver)
        self.gettopbrowser_page = GettopbrowserPage(self.driver)
        # self.header = Header(self.driver)
        # self.cancel_order_in_amazon = CancelOrderInAmazon(self.driver)
        # self.search_results_page = SearchResultsPage(self.driver)
        # #self.new_file_name = NewClassName(self.driver)
