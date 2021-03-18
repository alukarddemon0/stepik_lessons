from .base_page import BasePage
from .locators import ProductLocators, BasePageLocators
from .login_page import LoginPage


class ProductPage(BasePage):
    # Добавление товара в карзину
    def add_to_basket(self):
        # Arrange
        button_add_to_basket = self.browser.find_element(*ProductLocators.add_button_product)

        # Act
        button_add_to_basket.click()

    # Проверка на добавление офера
    def check_add_to_basket_offer(self):
        # Arrange
        message_add_to_basket_offer = self.browser.find_element(*ProductLocators.message_add_offer)

        # Assert
        assert BasePage.offer in message_add_to_basket_offer.text, 'Не добавлен по скидке'

    # Поиск и проверка совпадения имени продукта
    def check_name_product(self):
        # Arrange
        name_product = self.browser.find_element(*ProductLocators.product_name)
        message_name_product = self.browser.find_element(*ProductLocators.message_product_name)

        # Assert
        assert name_product.text == message_name_product.text, 'Имена таваров различаются'

    # Поиск и проверка совпадения цены продукта
    def check_price_product(self):
        # Arrange
        price_product = self.browser.find_element(*ProductLocators.product_price)
        message_price_product = self.browser.find_element(*ProductLocators.message_price)

        # Assert
        assert price_product.text == message_price_product.text, 'Цена не совпадает'

    # Проверка ссылки на страницу регистрации
    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.should_be_login_link()

    # Переход и проверка на странице регистрации
    def test_guest_can_go_to_login_page_from_product_page(self):
        # Arrange
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)

        # Act
        link.click()

        # Assert
        LoginPage(self.browser, self.url).should_be_login_page()

    # Проверка на отсутсвие сообщения усешного добавления товара на странице
    def should_not_be_success_message(self):
        # Assert
        assert self.is_not_element_present(*ProductLocators.message_product_success_add), \
            "Success message is presented, but should not be"

    # Проверка что сообщение усешного добавления товара пропадает со страници
    def should_be_gone_success_message(self):
        # Assert
        assert self.is_not_element_present(*ProductLocators.message_product_success_add), \
            "Сообщение не пропало"

    # Проверка сообщения об успешном добовлении на разных языках
    def check_lang_message(self, language):
        # Data
        text_add_success_product = {"ru": "был добавлен в вашу корзину", "en-gb": "has been added to your basket",
                                    "es": "ha sido añadido al carrito", "fr": "a été ajouté à votre panier"}

        # Arrange
        success_message = self.browser.find_element(*ProductLocators.message_product_success_add).text

        # Assert
        assert success_message == text_add_success_product[language], 'Сообщение не найдено'
