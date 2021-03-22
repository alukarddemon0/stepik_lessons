from .locators import SearchPageLocators
from .base_page import BasePage


class SearchPage(BasePage):
    # Data
    page_url = 'search/'

    def fiend_product(self, product_name):
        assert self.is_element_present(*SearchPageLocators().search_product(product_name))

    def should_be_search_page(self):
        assert BasePage.site_url in self.browser.current_url and self.page_url in self.browser.current_url, \
            'Не верная страница для поиска'