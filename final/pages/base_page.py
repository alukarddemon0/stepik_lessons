from locators import SearchPanelLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        # Arrange
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        # Act
        self.browser.get(self.url)

    def find_search_panel_send_product(self, name_product):
        # Arrange
        search_panel = self.browser.findfind_element(*SearchPanelLocators.field)
        search_button = self.browser.findfind_element(*SearchPanelLocators.search_button)

        # Act
        search_panel.sendkey(f'{name_product}')
        search_button.click()
