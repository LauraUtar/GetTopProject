from pages.gettopheader_page import GettopheaderPage

#
# class Gettopheader:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.gettopheader_page = GettopheaderPage(self.driver)

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.gettopheader_page = GettopheaderPage(self.driver)
        # self.header = Header(self.driver)
        # self.cancel_order_in_amazon = CancelOrderInAmazon(self.driver)
        # self.search_results_page = SearchResultsPage(self.driver)
        # #self.new_file_name = NewClassName(self.driver)
