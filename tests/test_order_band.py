import allure
from page_objects.order_page import OrderPage
from page_objects.main_page import MainPage
from conftest import *

class TestOrderBand:

    @allure.title('Тест счетчика "Выполнено за всё время"')
    @allure.description('Проверка, что при оформлении нового заказа счетчик "Выполнено за все время" увеличивается')
    def test_counter_all_time(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        with allure.step('Вход в аккаунт'):
            order_page.login()
        with allure.step('Переход на страницу "Лента заказов"'):
            main_page.get_band_page()
        with allure.step('Получить количество заказов в разделе "Выполнено за все время"'):
            count_1 = order_page.get_all_time()
        with allure.step('Совершить новый заказ'):
            order_page.new_order()
        with allure.step('Кликнуть на ленту заказов'):
            main_page.get_band_page()
        with allure.step('Проверить количество заказов в разделе "Выполнено за все время"'):
            count_2 = order_page.get_all_time()
            assert int(count_2) > int(count_1)


    @allure.title('Тест счетчика "Выполнено за сегодня"')
    @allure.description('Проверка, что при оформлении нового заказа счетчик "Выполнено за сегодня" увеличивается')
    def test_counter_today(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        with allure.step('Вход в аккаунт'):
            order_page.login()
        with allure.step('Переход на страницу "Лента заказов"'):
            main_page.get_band_page()
        with allure.step('Получить количество заказов в разделе "Выполнено за все время"'):
            count_1 = order_page.get_counter_value_today()
        with allure.step('Совершить новый заказ'):
            order_page.new_order()
        with allure.step('Кликнуть на ленту заказов'):
            main_page.get_band_page()
        with allure.step('Проверить количество заказов в разделе "Выполнено за сегодня"'):
            count_2 = order_page.get_counter_value_today()
            assert int(count_2) > int(count_1)


    @allure.title('Тест раздела "В работе"')
    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_section_in_work(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        with allure.step('Вход в аккаунт'):
            order_page.login()
        with allure.step('Совершить новый заказ'):
            order_page.new_order_long()
        with allure.step('Получить id заказа'):
            expected_id = order_page.get_order_id_from_details()
            order_page.click_cross_order()
        with allure.step('Переход в ленту заказов'):
            main_page.get_band_page()
        with allure.step('Проверка, что написано в столбце "В работе"'):
            real_id = order_page.get_ready_from_in_work()
        with allure.step('Проверить количество заказов в разделе "Выполнено за сегодня"'):
            assert int(expected_id) == int(real_id)


