from selenium.webdriver.common.by import By


class SearchPanelLocators():
    field = (By.XPATH, ("//*[@id = 'id_q']"))
    search_button = (By.XPATH, ("//input[@class = 'btn btn-default']"))


class SearchPageLocators():
    def search_product(self, product_name):
        selector = (By.XPATH, (f"//a[text()= ''{product_name}'']"))
        return selector
