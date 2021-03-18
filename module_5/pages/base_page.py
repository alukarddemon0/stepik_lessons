from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage():
    # Data
    site_url = 'http://selenium1py.pythonanywhere.com/'
    offer = 'Deferred benefit offer'

    def __init__(self, browser, url, timeout=10):
        # Arrange
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        # Act
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            # Act
            self.browser.find_element(how, what)

            # Assert
        except (NoSuchElementException):
            return False
        return True

    def go_to_login_page(self):
        # Act
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        # Assert
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        # Arrange
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        # Act
        alert.send_keys(answer)
        alert.accept()
        try:
            # Arrange
            alert = self.browser.switch_to.alert
            alert_text = alert.text

            # Act
            print(f"Your code: {alert_text}")
            alert.accept()

            # Assert
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            # Act
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))

            # Assert
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            # Act
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))

            # Assert
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        # Assert
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
