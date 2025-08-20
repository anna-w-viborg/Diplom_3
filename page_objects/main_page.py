import allure
import pytest
import selenium
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Diplom_3.page_objects.base_page import BasePage
from Diplom_3.locators import Locators
from Diplom_3.data import Data

class MainPage(BasePage):

    def get_main_page(self):
        self.go_to_url(Data.MAIN_URL)

    def get_band_page(self):
        self.go_to_url(Data.ORDER_BAND_URL)

    def click_order_band(self):
        self.click_element(Locators.ORDER_BAND_BUTTON)

    def click_constructor(self):
        self.click_element(Locators.CONSTRUCTOR_BUTTON)

    def wait_ready_header(self):
        self.wait_visibility_of_element(Locators.READY_HEADER)

    def wait_constructor_header(self):
        self.check_element_is_displayed(Locators.CONSTRUCTOR_HEADER)

    def click_x_sauce(self):
        self.click_element(Locators.X_SAUCE)

    def scroll_x_sauce(self):
        self.scroll_to_element(Locators.X_SAUCE)

    #def is_details(self):
     #   try:
      #      WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.DETAILS_OF_INGREDIENT))
       #     return True
        #except TimeoutException:
         #   return False

    def is_details(self):
        return self.check_element_is_displayed(Locators.DETAILS_OF_INGREDIENT)

    #def is_details(self):
       # self.check_element_is_displayed(Locators.DETAILS_OF_INGREDIENT)

    def click_details_cross(self):
        self.click_element(Locators.CROSS_EXIT)

    def get_count(self):
        return self.get_text_element(Locators.COUNTER)

    def get_counter(self):
        counter_text = self.get_text_element(Locators.COUNTER)
        if counter_text is None:
            raise Exception("Счетчик не найден на странице")
        return int(counter_text)

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        self.get_main_page()
        ingredient = self.wait_visibility_element(locator=Locators.X_SAUCE)
        basket = self.wait_visibility_element(locator=Locators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('')
    def wait_visibility_details(self):
        self.wait_visibility_of_element(Locators.DETAILS_OF_INGREDIENT)
