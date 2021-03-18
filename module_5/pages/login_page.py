from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):
    # Data
    page_url = 'login/'

    def should_be_login_page(self):
        # Assert
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

        # Проверка на верный url страници регистрации
    def should_be_login_url(self):
        # Assert
        assert BasePage.site_url in self.browser.current_url and self.page_url in self.browser.current_url, \
            'Не верная страница регистрации'

        # проверка, что есть форма логина
    def should_be_login_form(self):
        # Assert
        assert self.browser.find_element(*LoginPageLocators.login_email) and \
               self.browser.find_element(*LoginPageLocators.login_pass), 'Поле email или пароль не найдено'

        # проверка формы регистрации на странице
    def should_be_register_form(self):
        # Assert
        assert self.browser.find_element(*LoginPageLocators.reg_email) and \
               self.browser.find_element(*LoginPageLocators.reg_pass) and \
               self.browser.find_element(*LoginPageLocators.reg_pass_conf), 'Поле для регистрации не найдено'

    def register_new_user(self, email, password):
        # Arrange
        reg_email_field = self.browser.find_element(*LoginPage.reg_email)
        reg_pass_field = self.browser.find_element(*LoginPage.reg_pass)
        reg_pass_confirm_field = self.browser.find_element(*LoginPage.reg_pass_conf)
        reg_button_in_page = self.browser.find_element(*LoginPage.reg_button)

        # Act
        reg_email_field.send_keys(email)
        reg_pass_field.send_keys(password)
        reg_pass_confirm_field.send_keys(password)
        reg_button_in_page.click()
