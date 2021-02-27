import time

text_button_lang = {"ru": "Добавить в корзину", "en-gb": "Add to basket", "es": "Añadir al carrito",
                    "fr": "Ajouter au panier"}


def test_check_button(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    button_add = browser.find_element_by_xpath("//button[@class = 'btn btn-lg btn-primary btn-add-to-basket']")
    text_button = button_add.text
    assert text_button == text_button_lang[language], 'кнопка не найдена'
