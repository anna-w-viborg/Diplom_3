import pytest
from selenium import webdriver

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










#import pytest  # Обязательно импортируем pytest
#from selenium import webdriver
#import allure
#import allure_commons

#class WebdriverFactory:
#    @staticmethod
#    def get_webdriver(browser):
#        if browser == "Firefox":
#            return webdriver.Firefox()
#        elif browser == "Chrome":
#            return webdriver.Chrome()
#        else:
#            raise ValueError(f"Unsupported browser: {browser}")

# Эта функция добавляет возможность передачи параметра --browser в командной строке pytest
#def pytest_addoption(parser):
#    parser.addoption("--browser", action="store", default="Chrome", help="Выбор браузера: 'chrome' или 'firefox'.")

#@pytest.fixture
#def driver(request):
    # Получаем параметр браузера из командной строки
#    browser = request.config.getoption("--browser")
#    driver = WebdriverFactory.get_webdriver(browser)
#    driver.maximize_window()
#    yield driver
#    driver.quit()