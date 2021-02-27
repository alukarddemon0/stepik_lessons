import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru, en-gb, es, fr")
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope='function')
def language(request):
    language_page = request.config.getoption("language")
    if language_page not in ('ru', 'en-gb', 'es', 'fr'):
        raise pytest.UsageError('language not known')
    yield language_page


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    if browser_name not in ('chrome', 'firefox'):
        raise pytest.UsageError('browser not known')
    elif browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    else:
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
