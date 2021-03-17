from .base_page import BasePage
from .locators import ProductLocators, MainPageLocators
from .login_page import LoginPage


class ProductPage(BasePage):
    # Добавление товара в карзину
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductLocators.add_button_product)
        button_add_to_basket.click()

    # Проверка на добавление офера
    def check_add_to_basket_offer(self):
        message_add_to_basket_offer = self.browser.find_element(*ProductLocators.message_add_offer)
        assert BasePage.offer in message_add_to_basket_offer.text, 'Не добавлен по скидке'

    # Поиск и проверка совпадения имени продукта
    def check_name_product(self):
        name_product = self.browser.find_element(*ProductLocators.product_name)
        message_name_product = self.browser.find_element(*ProductLocators.message_product_name)
        assert name_product.text == message_name_product.text, 'Имена таваров различаются'

    # Поиск и проверка совпадения цены продукта
    def check_price_product(self):
        price_product = self.browser.find_element(*ProductLocators.product_price)
        message_price_product = self.browser.find_element(*ProductLocators.message_price)
        assert price_product.text == message_price_product.text, 'Цена не совпадает'

    # Проверка ссылки на страницу регистрации
    def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    # Переход и проверка на странице регистрации
    def test_guest_can_go_to_login_page_from_product_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        LoginPage.should_be_login_page()

    # Проверка на отсутсвие элимента на странице
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductLocators.message_add_offer), \
            "Success message is presented, but should not be"

    # Проверка что элемент пропадает со страници
    def should_be_gone_success_message(self):
        assert self.is_not_element_present(*ProductLocators.message_add_offer), \
            "Сообщение не пропало"
