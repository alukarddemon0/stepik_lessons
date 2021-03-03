import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru, en-GB, es, fr")
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope='function')
def language(request):
    language_page = request.config.getoption("language")
    if language_page not in ('ru', 'en-gb', 'es', 'fr'):
        raise pytest.UsageError('language not known')
    yield language_page


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
