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

from page_objects.base_page import BasePage
from locators import Locators
from data import Data
from page_objects.main_page import MainPage



class OrderPage(BasePage):

    def login(self):
        self.go_to_url(Data.LOGIN_URL)
        self.send_keys_to_field(Locators.EMAIL_FIELD, Data.EMAIL)
        self.send_keys_to_field(Locators.PASSWORD_FIELD, Data.PASSWORD)
        self.click_element(Locators.LOGIN_BUTTON)

    def click_order_band(self):
        self.click_element(Locators.ORDER_BAND_BUTTON)

    def click_cross_order(self):
        self.click_element(Locators.CROSS_EXIT_ORDER)

    def get_all_time(self):
        return self.get_text_element(Locators.ALL_TIME)

    def get_today(self):
        return self.get_text_element(Locators.TODAY)

    def get_counter_value_today(self):
        try:
            # Ожидание появления элемента
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(Locators.TODAY))
            # Получение текста и преобразование в число
            text = element.text.strip()
            if not text:
                raise ValueError("Элемент пуст")
            return int(text)
        except (TimeoutException, NoSuchElementException) as e:
            pass


    def get_text_in_ready(self):
        try:
            # Ожидание появления элемента
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(Locators.LIST_IN_WORK))
            # Получение текста и
            text = element.text()
            if not text:
                raise ValueError("Элемент пуст")
            return text
        except (TimeoutException, NoSuchElementException) as e:
            pass




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

    def get_main_page(self):
        self.go_to_url(Data.MAIN_URL)


    def get_order_id_from_details(self):
        self.find_and_wait_until_id_changes(Locators.ORDER_ID,"9999")
        return self.get_text_from_id()

    def find_and_wait_until_id_changes(self, locator, initial_text='9999', timeout=30):
        start_time = time.time()
        current_text = initial_text
        while time.time() - start_time < timeout:
            try:
                element = self.find_id_with_wait()
                current_text = element.text.strip()
                if current_text != initial_text:
                    return element
                time.sleep(0.5)  # небольшая пауза перед следующей проверкой
            except (TimeoutException, NoSuchElementException):
                continue
        raise TimeoutException(f"Текст элемента не изменился за {timeout} секунд")

    def find_id_with_wait(self):
        try:
            return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(Locators.ORDER_ID))
        except (TimeoutException, NoSuchElementException) as e:
            pass
            return None

    def get_text_from_id(self):
        element = self.find_id_with_wait()
        if element:
            return element.text.strip()
        return None



    def get_ready_from_in_work(self):
        self.find_and_wait_until_in_work_changes(Locators.LIST_IN_WORK, "Все текущие заказы готовы!")
        return self.get_text_from_in_work()

    def find_and_wait_until_in_work_changes(self, locator, initial_text='Все текущие заказы готовы!', timeout=30):
        start_time = time.time()
        current_text = initial_text
        while time.time() - start_time < timeout:
            try:
                element = self.find_in_work_with_wait()
                current_text = element.text.strip()
                if current_text != initial_text:
                    return element
                time.sleep(0.5)  # небольшая пауза перед следующей проверкой
            except (TimeoutException, NoSuchElementException):
                continue
        raise TimeoutException(f"Текст элемента не изменился за {timeout} секунд")

    def find_in_work_with_wait(self):
        try:
            return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(Locators.LIST_IN_WORK))
        except (TimeoutException, NoSuchElementException) as e:
            pass
            return None

    def get_text_from_in_work(self):
        element = self.find_in_work_with_wait()
        if element:
            return element.text.strip()
        return None

