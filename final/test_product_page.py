from .pages.product_page import AddLogicProduct


class TestProductAdd:
    def test_add_button(self, language, browser):
        # Data
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hackers-painters_185/'

        # Arrange
        page = AddLogicProduct(browser, link)
        page.open()

        # Assert
        page.check_status(language)
        page.should_not_be_button_add()

    def test_no_add_wish_list(self, browser):
        # Data
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hackers-painters_185/'

        # Arrange
        page = AddLogicProduct(browser, link)
        page.open()

        # Assert
        page.unauthorized_no_add_collection()

    def test_screen_product(self, browser):
        # Data
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/visual-guide-to-lock-picking_206/'

        # Arrange
        page = AddLogicProduct(browser, link)
        page.open()

        # Assert
        page.no_screen_on_product()