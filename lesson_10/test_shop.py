import allure
import pytest
from selenium import webdriver
from shop_page import StandardPage, InventoryPage, CartPage, CheckoutPage


# Фикстура для автоматического запуска и закрытия браузера Firefox
@pytest.fixture
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


@allure.feature("Интернет-магазин")
@allure.title("Проверка функциональности интернет-магазина")
@allure.description("Тест проверяет авторизацию, "
                    "добавление 3-х товаров в корзину, "
                    "оформление заказа и финальную стоимость")
@allure.severity(allure.severity_level.CRITICAL)
def test_ecommerce_purchase_flow(driver):
    # 1. Первый шаг.
    with allure.step("Открываем главную страницу"):
        driver.get('https://saucedemo.com/')

    # 2. Второй шаг. Авторизоваться как пользователь standard_user.
    with allure.step('Авторизоваться как пользователь standard_user'):
        login_page = StandardPage(driver)
        login_page.login('standard_user', 'secret_sauce')

    # 3. Третий шаг. Добавить в корзину товары:
    # Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie.
    with allure.step('Добавить в корзину товары'):
        inventory_page = InventoryPage(driver)

        with allure.step('Добавляем Sauce Labs Backpack'):
            inventory_page.Backpack_button()

        with allure.step('Добавляем Sauce Labs Bolt T-Shirt'):
            inventory_page.Bolt_T_Shirt_button()

        with allure.step('Добавляем Sauce Labs Onesie'):
            inventory_page.onesie_button()

    # 4. Четвертый шаг. Переходим в корзину.
    with allure.step('Перейти в карзину'):
        inventory_page.basket_button()

    # 5. Пятый шаг.  Нажимаем  кнопку Checkout.
    with allure.step('Нажать кнопку Checkout'):
        cart_page = CartPage(driver)
        cart_page.get_item_names()
        cart_page.checkout_button()

    # 6. Шестой шаг. Заполняем форму своими данными:
    with allure.step('Заполнить форму своими данными: '
                     'имя, фамилия, почтовый индекс'):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form(
            'Vera',
            'Ivanova',
            '424910'
        )

        checkout_page.continue_button()

    # 7. Читаем со страницы итоговую стоимость (Total).
    with allure.step('Прочитать со страницы итоговую стоимость (Total)'):
        total_text = checkout_page.get_total_price_text()

    # 8. Проверяем, что итоговая сумма равна $58.29.
    with allure.step('Проверяем, что итоговая сумма равна $58.29'):
        assert total_text == "Total: $58.29"

    # Открыть сайт магазина.
    # Авторизоваться как пользователь standard_user.
    # Добавить в корзину товары:
    # Sauce Labs Backpack.
    # Sauce Labs Bolt T-Shirt.
    # Sauce Labs Onesie.
    # Перейти в корзину.
    # Нажать кнопку Checkout.
    # Заполнить форму своими данными:
    # Имя.
    # Фамилия.
    # Почтовый индекс.
    # Прочитать со страницы итоговую стоимость (Total).
    # Закрыть браузер.
    # Проверить (assert), что итоговая сумма равна $58.29.
