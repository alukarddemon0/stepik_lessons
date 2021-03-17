import pytest
from .pages.product_page import ProductPage


class TestProductPage:
    offers = ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
              pytest.param("offer7", marks=pytest.mark.xfail),
              "offer8", "offer9"]

    @pytest.mark.parametrize('promo_offer', offers)
    def test_add_to_basket(self, browser, promo_offer):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}'
        page_product = ProductPage(browser, link)
        page_product.open()
        page_product.add_to_basket()
        page_product.solve_quiz_and_get_code()
        page_product.check_name_product()
        page_product.check_price_product()
        page_product.check_add_to_basket_offer()
