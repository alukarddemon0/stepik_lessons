import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# принимает язык для браузера и сам тип браузера
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose language: ru, en-GB, es, fr")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


# Проверка введеного языка и возврат его значения
@pytest.fixture(scope='function')
def language(request):
    language_page = request.config.getoption("language")
    if language_page not in ('ru', 'en-GB', 'es', 'fr'):
        raise pytest.UsageError('language not known')
    yield language_page


# Настройки и тип браузера
@pytest.fixture(scope="function")
def browser(request, language):
    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    if browser_name not in ('chrome', 'firefox'):
        raise pytest.UsageError('browser not known')
    elif browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('promo_offer',
["offer0","offer1","offer2","offer3","offer4","offer5","offer6","offer7","offer8","offer9"])
