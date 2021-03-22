from .pages.search_page import SearchPage
import pytest


class TestSearchPage:
    arguments = ['', 'catalogue/', 'accounts/login/', 'basket/', 'offers/']

    @pytest.mark.parametrize('urls', arguments)
    def test_search_any_page(self, browser, urls):
        # Data
        link = f"http://selenium1py.pythonanywhere.com/{urls}"
        product_name = "Hacking Exposed Wireless"

        # Arrange
        page = SearchPage(browser, link)
        page.open()

        # Act
        page.find_search_panel_send_product(product_name)

        # Assert
        page.should_be_search_page()
        page.fiend_product(product_name)
