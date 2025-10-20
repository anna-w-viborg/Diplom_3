import allure
from Diplom_3.page_objects.main_page import MainPage
from Diplom_3.conftest import *
from Diplom_3.urls import Urls


class TestFunctional:

    @allure.title('Проверка всплывающего окна ингредиента')
    @allure.description('Проверка, что при клике на ингредиент появляется всплывающее окно с информацией об ингредиенте')
    def test_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        with allure.step('Открытие главной страницы'):
            main_page.get_main_page()
        with allure.step('Скроллим до элемента x-sauce'):
            main_page.scroll_x_sauce()
        with allure.step('Клик на "Х-соус"'):
            main_page.click_x_sauce()
        with allure.step('Проверка, что окно с деталями отображается'):
            assert main_page.is_details()

    @allure.title('Тест увеличения счетчика при добавлении продуктов')
    @allure.description('Проверка, что когда продукт добавляется в бургер, его счетчик увеличивается')
    def test_add_ingredient_counter_becomes(self, driver):
        main_page = MainPage(driver)
        with allure.step('Открытие главной страницы'):
            main_page.get_main_page()
        with allure.step('Проверка, что отображается страница с конструктором'):
            main_page.wait_constructor_header()
        with allure.step('Скроллим до элемента x-sauce'):
            main_page.scroll_x_sauce()
        with allure.step('Получаем значение счетчика'):
            count_1 = main_page.get_count()
        with allure.step('Перетаскиваем соус в бургер'):
            main_page.put_ingredient_into_basket()
        with allure.step('Проверяем, изменилось ли значение счетчика'):
            count_2 = main_page.get_count()
            assert int(count_2) == int(count_1) + 1


    @allure.title('Переход в конструктор')
    @allure.description('Проверка, что по клику на кнопку "Конструктор" просходит переход в конструктор бургера')
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        with allure.step('Открытие страницы "Лента заказов"'):
            main_page.get_band_page()
        with allure.step('Клик по кнопке "Конструктор"'):
            main_page.click_constructor()
        with allure.step('Проверка, что отображается страница с конструктором'):
            assert main_page.get_current_url() == Urls.MAIN_URL


    @allure.title('Переход в ленту заказов')
    @allure.description('Проверка, что по клику на кнопку "Лента заказа" происходит переход на страницу с историей заказов')
    def test_order_band_button(self, driver):
        main_page = MainPage(driver)
        with allure.step('Открытие главной страницы'):
            main_page.get_main_page()
        with allure.step('Клик по кнопке "Лента заказов'):
            main_page.click_order_band()
        with allure.step('Проверка, что загрузилась страница с лентой заказов'):
            assert main_page.get_current_url() == f"{Urls.MAIN_URL}{Urls.ORDER_BAND_URL}"


    @allure.title('Тест закрытия деталей ингредиента')
    @allure.description('Проверка, что при нажатии на крестик окно с деталями ингредиента закрывается')
    def test_cross_exit_details_window(self, driver):
        main_page = MainPage(driver)
        with allure.step('Открытие главной страницы'):
            main_page.get_main_page()
        with allure.step('Проверка, что отображается страница с конструктором'):
            main_page.wait_constructor_header()
        with allure.step('Скроллим до элемента x-sauce'):
            main_page.scroll_x_sauce()
        with allure.step('Клик на "Х-соус"'):
            main_page.click_x_sauce()
        with allure.step('Проверка, что окно с деталями отображается'):
            main_page.is_details()
        with allure.step('Клик по крестику'):
            main_page.click_details_cross()
        with allure.step('Проверка, что окно с деталями не отображается'):
            assert main_page.is_details()



