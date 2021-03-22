from .locators import SearchPanelLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    # Data
    site_url = 'http://selenium1py.pythonanywhere.com/'

    def __init__(self, browser, url, timeout=10):
        # Arrange
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            # Act
            self.browser.find_element(how, what)

            # Assert
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        # Act
        self.browser.get(self.url)

    def is_not_element_present(self, how, what, timeout=4):
        try:
            # Act
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))

            # Assert
        except TimeoutException:
            return True

        return False

    def find_search_panel_send_product(self, name_product):
        # Arrange
        search_panel = self.browser.find_element(*SearchPanelLocators.field)
        search_button = self.browser.find_element(*SearchPanelLocators.search_button)

        # Act
        search_panel.send_keys(f'{name_product}')
        search_button.click()
