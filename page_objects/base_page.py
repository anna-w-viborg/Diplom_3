import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from seletools.actions import drag_and_drop

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Ждем, когда элемент будет видно')
    def wait_visibility_of_element(self, locator):
        self.driver.find_element(locator)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(locator).click()

   # @allure.step('Заполнить поле данными')
   # def send_keys_to_field(self, locator, keys):
    #    self.driver.find_element(locator).send_keys(keys)

    def send_keys_to_field(self, locator, keys):
        try:
            # Распаковываем кортеж локатора
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locator)
            )
            element.send_keys(keys)
        except Exception as e:
            logging.error(f"Ошибка при отправке ключей: {str(e)}")
            raise

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, locator):
        return self.driver.find_element(locator).text

    @allure.step('Переключиться на другое окно')
    def switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить заголовок страницы')
    def get_page_title(self, title_of_page):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(title_of_page))
        return self.driver.title

    @allure.step('Проверить, что элемент точно отображается')
    def check_element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Получить текущий url')
    def get_current_url (self):
        return self.driver.current_url

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('')
    def go_to_url(self, locator):
        return self.driver.get(locator)

    def get_text_element(self, locator):          # Распаковываем кортеж локатора
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return element.text


    def wait_visibility_element(self, locator):
        try:
            return WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located(locator)
                )
        except TimeoutException:
            raise Exception(f"Элемент не найден: {locator}")

#    def get_text_element_2(self, locator):
 #       try:
  #          element = WebDriverWait(self.driver, 20).until(
   #             EC.visibility_of_element_located(locator)
    #        )
     #       return element.text
      #  except (TimeoutException):
       #     return None