from selenium.webdriver.common.by import By



class Locators:

    #ЛОКАТОРЫ ГЛАВНОЙ СТРАНИЦЫ
    #кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    #страница на которую ведет клик по "Конструктору" с заглолвком "Соберите бургер"
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    #кнопка "Лента заказов"
    ORDER_BAND_BUTTON = (By.XPATH, "//p[contains(text(),'Лента')]")
    #страница на которую ведет клик по "Лента заказов"
    READY_HEADER = (By.XPATH, "//p[contains(text(), 'Готовы:')]")
    #кнопка ингредиента x-sauce
    INGREDIENT_BUTTON = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mb-8')]")


    BUN = (By.XPATH, '//a[contains(@href, "bdaaa6d")]')
    X_SAUCE = (By.XPATH, '//a[contains(@href, "bdaaa72")]')
    #всплывающее окно ингредиента
    DETAILS_OF_INGREDIENT = (By.XPATH, '//h2[contains(text(), "Детали")]')
    #информация об ингредиенте

    CROSS_EXIT_ORDER = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    #крестик закрытия окна информации об ингредиенте
    CROSS_EXIT = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified__3V5XS")]')
    #счетчик ингредиента x-sauce
    COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']/div[@class='counter_counter__ZNLkj counter_default__28sqi']/p[@class='counter_counter__num__3nue1']")
    #COUNTER = (By.XPATH, '//a[contains(@href, "bdaa72")]')
    BASKET = (By.XPATH, '//img[@alt="Перетяните булочку сюда (верх)"]')


    #
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    #
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    #
    ALL_TIME = (By.XPATH, '//div[@class="undefined mb-15"]//p[contains(@class, "OrderFeed_number")]')
    TODAY = (By.XPATH, '//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
#p[contains(text(), "за сегодня")]//
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(), "Оформить")]')

    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")

    LIST_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li[1]")




