import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()

