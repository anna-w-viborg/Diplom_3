from datetime import time
import time
import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from setuptools import logging

from Diplom_3.page_objects.base_page import BasePage
from Diplom_3.locators import Locators
from Diplom_3.data import Data
from Diplom_3.page_objects.main_page import MainPage
from Diplom_3.urls import Urls


class OrderPage(BasePage):

    @allure.step('Авторизация зарегистрированного пользователя')
    def login(self, email, password):
        self.go_to_url(f"{Urls.MAIN_URL}{Urls.LOGIN_URL}")
        self.send_keys_to_field(Locators.EMAIL_FIELD, email)
        self.send_keys_to_field(Locators.PASSWORD_FIELD, password)
        self.click_element(Locators.LOGIN_BUTTON)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_order_band(self):
        self.click_element(Locators.ORDER_BAND_BUTTON)

    @allure.step('Клик на крестик закрытия окна заказа')
    def click_cross_order(self):
        self.click_element(Locators.CROSS_EXIT_ORDER)

    @allure.step('Получение значения счетчика вполненных за все время заказов')
    def get_all_time(self):
        return self.get_text_element(Locators.ALL_TIME)

    @allure.step('Получение значения выполненных за сегодня заказов')
    def get_today(self):
        return self.get_text_element(Locators.TODAY)

    @allure.step('Получение значения счетчика выполненных за сегодня заказов')
    def get_counter_value_today(self):
        self.get_counter_done(Locators.TODAY)

    @allure.step('Получение текста из списка "В работе"')
    def get_text_in_ready(self):
        self.get_text_list(Locators.LIST_IN_WORK)



    @allure.step('Оформление нового заказа')
    def new_order(self):
        self.click_element(Locators.CONSTRUCTOR_BUTTON)
        #кликнуть конструктор
        #перетащить х соус
        self.put_ingredient_into_basket()
        self.put_bun_into_basket()#оформить заказ
        self.click_element(Locators.MAKE_ORDER_BUTTON)
        self.click_element(Locators.CROSS_EXIT_ORDER)
        #self.go_to_url(Data.ORDER_BAND_URL)
        #
        #
    @allure.step('Оформление нового заказа')
    def new_order_long(self):
        self.click_element(Locators.CONSTRUCTOR_BUTTON)
        #кликнуть конструктор
        #перетащить х соус
        self.put_ingredient_into_basket()
        self.put_bun_into_basket()#оформить заказ
        self.click_element(Locators.MAKE_ORDER_BUTTON)

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        self.get_main_page()
        ingredient = self.wait_visibility_element(locator=Locators.X_SAUCE)
        basket = self.wait_visibility_element(locator=Locators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Перетащить элемент в корзину')
    def put_bun_into_basket(self):
        ingredient = self.wait_visibility_element(locator=Locators.BUN)
        basket = self.wait_visibility_element(locator=Locators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Переход на адрес главной страницы')
    def get_main_page(self):
        self.go_to_url(Urls.MAIN_URL)

    @allure.step('Получение номера заказа из окна с деталями заказа')
    def get_order_id_from_details(self):
        self.find_and_wait_until_id_changes(Locators.ORDER_ID,"9999")
        return self.get_text_from_id()

    @allure.step('Ожидание, пока появится номер заказа')
    def find_and_wait_until_id_changes(self):
        self.wait_change(Locators.ORDER_ID, initial_text='9999', timeout=30)


    @allure.step('Получение id заказа с ожиданием')
    def find_id_with_wait(self):
        self.find_text(Locators.ORDER_ID)

    @allure.step('Получение текста id заказа')
    def get_text_from_id(self):
        element = self.find_id_with_wait()
        if element:
            return element.text.strip()
        return None

    @allure.step('Получение значения в столбце "В работе"')
    def get_ready_from_in_work(self):
        self.find_and_wait_until_in_work_changes(Locators.LIST_IN_WORK, "Все текущие заказы готовы!")
        return self.get_text_from_in_work()

    @allure.step('Ожидание, пока в столбце "В работе" появится номер заказа')
    def find_and_wait_until_in_work_changes(self):
        self.wait_change(Locators.LIST_IN_WORK, initial_text='Все текущие заказы готовы!', timeout=30)

    @allure.step('Ожидание видимости списка "В работе"')
    def find_in_work_with_wait(self):
        self.find_text(Locators.LIST_IN_WORK)

    @allure.step('Получение текста номера последнего заказа из списка "В работе"')
    def get_text_from_in_work(self):
        element = self.find_in_work_with_wait()
        if element:
            return element.text.strip()
        return None

