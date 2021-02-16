from selenium import webdriver
import time


main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
registration_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_current_registration_page():
    # Data
    registration_button = "login_link"

    try:

        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        # Act
        current_page = browser.current_url

        # Assert
        assert main_page_link == current_page, \
            "the current page is not the requested page"

        # Act
        browser.find_element_by_id(registration_button).click()
        current_page = browser.current_url

        # Assert
        assert registration_page_link == current_page, \
            "the current page is not the requested page"

    finally:
        browser.quit()


def back_main_page():
    # Data
    link_main_page = "//a[text()='Начало']"
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(registration_page_link)

        # Act
        current_page = browser.current_url

        # Assert
        assert registration_page_link == current_page, \
            "the current page is not the requested page"

        # Act
        browser.find_element_by_xpath(link_main_page).click()
        current_page = browser.current_url

        # Assert
        assert main_page_link == current_page, \
            "the current page is not the requested page"

    finally:
        browser.quit()


test_current_registration_page()
back_main_page()
