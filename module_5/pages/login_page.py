from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):
    page_url = 'login/'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на верный url страници регистрации
        assert BasePage.site_url in self.browser.current_url and self.page_url in self.browser.current_url,\
            'Не верная страница регистрации'

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.login_email) and \
               self.browser.find_element(*LoginPageLocators.login_pass), 'Поле email или пароль не найдено'

    def should_be_register_form(self):
        # проверка формы регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.reg_email) and \
               self.browser.find_element(*LoginPageLocators.reg_pass) and \
               self.browser.find_element(*LoginPageLocators.reg_pass_conf), 'Поле для регистрации не найдено'
