def test_check_button(browser, language):
    # Data
    text_button_lang = {"ru": "Добавить в корзину", "en-gb": "Add to basket", "es": "Añadir al carrito",
                        "fr": "Ajouter au panier"}
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    selector_button = "//button[@class = 'btn btn-lg btn-primary btn-add-to-basket']"

    # Arrange
    browser.get(link)

    # Act
    button_add = browser.find_element_by_xpath(selector_button).text

    # Assert
    assert button_add == text_button_lang[language], 'кнопка не найдена'
