import pytest
from selenium import webdriver
from data import Data


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser):
        if browser == "Firefox":
            return webdriver.Firefox()
        elif browser == "Chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

# Добавляем только опцию для браузера

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="Chrome",
        help="Выбор браузера: 'chrome' или 'firefox'"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()




