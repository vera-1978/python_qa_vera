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
    # Авторизоваться как пользователь standard_user.
    driver.get('https://saucedemo.com')
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
    inventory_page.basket_button()






# Перейти в корзину.
# Нажать кнопку Checkout.
# Заполнить форму своими данными:
# Имя.
# Фамилия.
# Почтовый индекс.
# Прочитать со страницы итоговую стоимость (Total).
# Закрыть браузер.
# Проверить (assert), что итоговая сумма равна $58.29.