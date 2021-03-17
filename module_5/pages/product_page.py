from .base_page import BasePage
from .locators import ProductLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductLocators.add_button_product)
        button_add_to_basket.click()

    def check_add_to_basket_offer(self):
        message_add_to_basket_offer = self.browser.find_element(*ProductLocators.message_add_offer)
        assert BasePage.offer in message_add_to_basket_offer.text, 'Не добавлен по скидке'

    def check_name_product(self):
        name_product = self.browser.find_element(*ProductLocators.product_name)
        message_name_product = self.browser.find_element(*ProductLocators.message_product_name)
        assert name_product.text == message_name_product.text, 'Имена таваров различаются'

    def check_price_product(self):
        price_product = self.browser.find_element(*ProductLocators.product_price)
        message_price_product = self.browser.find_element(*ProductLocators.message_price)
        assert price_product.text == message_price_product.text, 'Цена не совпадает'
