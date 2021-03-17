from .pages.product_page import ProductPage


class TestProductPage:
    def test_add_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page_product = ProductPage(browser, link)
        page_product.open()
        page_product.add_to_basket()
        page_product.solve_quiz_and_get_code()
        page_product.check_name_product()
        page_product.check_price_product()
        page_product.check_add_to_basket_offer()