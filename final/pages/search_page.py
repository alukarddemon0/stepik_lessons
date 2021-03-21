from locators import SearchPageLocators
from base_page import BasePage


class SearchPage(BasePage):

    def fiend_product(self, product_name):
        search_product = self.browser.findfind_element(*SearchPageLocators().search_product(product_name))
