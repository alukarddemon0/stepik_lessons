from selenium.webdriver.common.by import By


class SearchPanelLocators():
    field = (By.XPATH, ("//*[@id = 'id_q']"))
    search_button = (By.XPATH, ("//input[@class = 'btn btn-default']"))


class SearchPageLocators():
    def search_product(self, product_name):
        selector = (By.XPATH, (f"//a[text()= \"{product_name}\"]"))
        return selector


class ProductLocators():
    add_button_product = (By.XPATH, ("//*[@id= 'add_to_basket_form']/button"))
    status_product = (By.XPATH, ("//p[contains(@class, 'outofstock')]"))
    add_wish_list_disabled = (By.XPATH, ("//button[@class='btn btn-lg btn-wishlist'][@disabled]"))
    no_screen = (By.XPATH, ("//img[@src='/media/cache/59/d3/59d3d8c74e03cbba3aed4051c18d6a8c.jpg']"))