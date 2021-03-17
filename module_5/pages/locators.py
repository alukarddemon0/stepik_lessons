from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    login_email = (By.CSS_SELECTOR, '#id_login-username')
    login_pass = (By.CSS_SELECTOR, '#id_login-password')
    reg_email = (By.CSS_SELECTOR, '#id_registration-email')
    reg_pass = (By.CSS_SELECTOR, '#id_registration-password1')
    reg_pass_conf = (By.CSS_SELECTOR, '#id_registration-password2')


class ProductLocators():
    product_price = (By.XPATH, ("//*[@class= 'price_color']"))
    product_name = (By.XPATH, ("//*[@class= 'col-sm-6 product_main']/h1"))
    add_button_product = (By.XPATH, ("//*[@id= 'add_to_basket_form']/button"))
    message_product_name = (By.XPATH, ("//*[@id='messages']/div[1]/div/strong"))
    message_price = (By.XPATH, ("//*[@id='messages']/div[3]/div/p[1]/strong"))
    message_add_offer = (By.XPATH, ("//*[@id='messages']/div[2]/div/strong"))