from .pages.search_page import SearchPage

link = "http://selenium1py.pythonanywhere.com"
product_name = "The shellcoder's handbook"


class TestMainPage:
    def test_search_main_page(self, browser):
        # Arrange
        page = SearchPage(browser, link)
        page.open()
        page.find_search_panel_send_product(product_name)
        page.fiend_product(product_name)