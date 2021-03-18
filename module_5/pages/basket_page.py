from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def go_to_basket(self):
        # Arrange
        basket_button = self.browser.find_element(*BasketLocators.basket_button)

        # Act
        basket_button.click()

    def check_product_in_basket(self):
        # Data
        message = 'Your basket is empty'

        # Arrange
        find_message = self.browser.find_element(*BasketLocators.message_no_product).text

        # Assert
        assert self.is_not_element_present(*BasketLocators.have_product), 'Товар найден'
        assert message in find_message, 'Корзина не пустая'
