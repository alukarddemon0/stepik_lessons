import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


class TestProductPage:
    # Data
    offers = ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
              pytest.param("offer7", marks=pytest.mark.xfail),
              "offer8", "offer9"]

    @pytest.mark.parametrize('promo_offer', offers)
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Data
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}'

        # Arrange
        page_product = ProductPage(browser, link)
        page_product.open()

        # Act
        page_product.add_to_basket()
        page_product.solve_quiz_and_get_code()

        # Assert
        page_product.check_name_product()
        page_product.check_price_product()
        page_product.check_add_to_basket_offer()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Data
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

        # Arrange
        page_product = ProductPage(browser, link)
        page_product.open()

        # Act
        page_product.add_to_basket()

        # Assert
        page_product.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # Data
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

        # Arrange
        page_product = ProductPage(browser, link)
        page_product.open()

        # Assert
        page_product.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Data
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

        # Arrange
        page_product = ProductPage(browser, link)
        page_product.open()

        # Act
        page_product.add_to_basket()

        # Assert
        page_product.should_be_gone_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.test_guest_can_go_to_login_page_from_product_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

        # Arrange
        page = BasketPage(browser, link)
        page.open()

        # Act
        page.go_to_basket()

        # Assert
        page.check_product_in_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Data
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        password = '123456789ASDFGTQWER'

        # Arrange
        page = LoginPage(browser, link)
        page.open()

        # Act
        page.register_new_user(email, password)

        # Assert
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Data
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

        # Arrange
        page_product = ProductPage(browser, link)
        page_product.open()

        # Assert
        page_product.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # Data
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

        # Arrange
        page_product = ProductPage(browser, link)
        page_product.open()

        # Act
        page_product.add_to_basket()

        # Assert
        page_product.check_name_product()
        page_product.check_price_product()
        page_product.check_add_to_basket_offer()
