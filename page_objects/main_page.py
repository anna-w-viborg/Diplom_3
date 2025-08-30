import allure
import pytest
import selenium
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Diplom_3.page_objects.base_page import BasePage
from Diplom_3.locators import Locators
from Diplom_3.data import Data
from Diplom_3.urls import Urls

class MainPage(BasePage):

    @allure.step('Переход на адрес главной страницы')
    def get_main_page(self):
        self.go_to_url(Urls.MAIN_URL)

    @allure.step('Переход на адрес ленты заказов')
    def get_band_page(self):
        self.go_to_url(f"{Urls.MAIN_URL}{Urls.ORDER_BAND_URL}")

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_order_band(self):
        self.click_element(Locators.ORDER_BAND_BUTTON)

    @allure.step('Клик на кнопку "Конструктор"')
    def click_constructor(self):
        self.click_element(Locators.CONSTRUCTOR_BUTTON)

    @allure.step('Ожидание видимости заголовка "Готовы"')
    def wait_ready_header(self):
        self.wait_visibility_of_element(Locators.READY_HEADER)

    @allure.step('Ожидание видимости заголовка конструктора')
    def wait_constructor_header(self):
        self.check_element_is_displayed(Locators.CONSTRUCTOR_HEADER)

    @allure.step('Клик по ингредиенту "Х-соус"')
    def click_x_sauce(self):
        self.click_element(Locators.X_SAUCE)

    @allure.step('Скролл до ингредиента "Х-соус"')
    def scroll_x_sauce(self):
        self.scroll_to_element(Locators.X_SAUCE)

    @allure.step('Проверка, что отображается окно с подробной информацией об ингредиенте')
    def is_details(self):
        return self.check_element_is_displayed(Locators.DETAILS_OF_INGREDIENT)

    @allure.step('Клик по крестику для закрытия окна с информацией об ингредиенте')
    def click_details_cross(self):
        self.click_element(Locators.CROSS_EXIT)

    @allure.step('Получение значения счетчика ингредиента')
    def get_count(self):
        return self.get_text_element(Locators.COUNTER)

    @allure.step('Получение значения счетчика ингредиента')
    def get_counter(self):
        counter_text = self.get_text_element(Locators.COUNTER)
        if counter_text is None:
            raise Exception("Счетчик не найден на странице")
        return int(counter_text)

    @allure.step('Перетаскивание элемента в корзину')
    def put_ingredient_into_basket(self):
        self.get_main_page()
        ingredient = self.wait_visibility_element(locator=Locators.X_SAUCE)
        basket = self.wait_visibility_element(locator=Locators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Ожидание видимости окна с подробной информацией об ингредиенте')
    def wait_visibility_details(self):
        self.wait_visibility_of_element(Locators.DETAILS_OF_INGREDIENT)


