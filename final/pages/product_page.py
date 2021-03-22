from .base_page import BasePage
from .locators import ProductLocators


class AddLogicProduct(BasePage):
    def check_status(self, language):
        # Data
        status_lang = {"ru": "Недоступно", "en-GB": "Unavailable", "es": "No disponible",
                       "fr": "Non disponible"}
        # Arrange
        status = self.browser.find_element(*ProductLocators.status_product).text

        # Assert
        assert status_lang[language] in status, 'неверный статус'

    def should_not_be_button_add(self):
        # Assert
        assert self.is_not_element_present(*ProductLocators.add_button_product), \
            "Кнопка найдена, но не должна"

    def unauthorized_no_add_collection(self):
        # Assert
        assert self.browser.find_element(
            *ProductLocators.add_wish_list_disabled), 'Можно добавить в коллекцию или книга закрыта'

    def no_screen_on_product(self):
        assert self.browser.find_element(*ProductLocators.no_screen), 'У книги есть скрин обложки'
