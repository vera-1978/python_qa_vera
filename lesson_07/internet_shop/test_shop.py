import pytest
from selenium import webdriver
from lesson_07.internet_shop.shop_page import ShopPage, StandardPage, InventoryPage, CartPage, CheckoutPage


# Фикстура для автоматического запуска и закрытия браузера Firefox
@pytest.fixture
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()

def test_ecommerce_purchase_flow(driver):
    # Открыть сайт магазина.
    driver.get('https://saucedemo.com')

    # Авторизоваться как пользователь standard_user.
    login_page = StandardPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    # Добавить в корзину товары:
    # Sauce Labs Backpack.
    # Sauce Labs Bolt T-Shirt.
    # Sauce Labs Onesie.
    inventory_page = InventoryPage(driver)
    inventory_page.Backpack_button()
    inventory_page.Bolt_T_Shirt_button()
    inventory_page.onesie_button()

    # Перейти в карзину.
    inventory_page.basket_button()

    # Нажать кнопку Checkout.
    cart_page = CartPage(driver)
    cart_page.get_item_names()
    cart_page.checkout_button()

    # Заполнить форму своими данными:
    # имя, фамилия, почтовый индекс.
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form(
        'Vera',
        'Ivanova',
        '424910'
    )

    checkout_page.continue_button()

    # Прочитать со страницы итоговую стоимость (Total).
    total_text = checkout_page.get_total_price_text()

    # Проверить (assert), что итоговая сумма равна $58.29.
    assert total_text == "Total: $58.29"
