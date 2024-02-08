import pytest
from selenium import webdriver
from _pytest.config import UsageError
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Choose language")


@pytest.fixture
def browser(request):
    user_language = request.config.getoption("--language")

    if user_language is None:
        raise UsageError("Нужно запускать через терминал!"
                         "Попробуйте ввести следующую команду: pytest -sv --language=es test_items.py")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print(f"\nrun test in {user_language}")
    driver = webdriver.Chrome(options=options)
    yield driver
    print(f"\nfinish test in {user_language}")
    driver.quit()
