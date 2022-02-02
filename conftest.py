import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Chose language:')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_lang = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_lang)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox"
                                "--language should be ru, en, fr, es")
    yield browser
    browser.quit()
