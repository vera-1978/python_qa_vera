from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Создание класса для страницы авторизации содержаций
    # методы для ввода логина и пароля,
    # а также для нажатия кнопки входа.


class StandardPage(ShopPage):
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def login(self, username, password):

        self.wait.until(EC.visibility_of_element_located(
            self.INPUT_USERNAME)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(
            self.INPUT_PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    # Создание класс для главной страницы магазина,
    # который будет содержать методы для добавления
    # товаров в корзину и перехода в корзину;


class InventoryPage(ShopPage):
    BACKPACK_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BOLT_T_SHIRT_BUTTON = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ONESIE_BUTTON = (By.ID, 'add-to-cart-sauce-labs-onesie')
    BASKET_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')

    def Backpack_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_BUTTON)).click()

    # Sauce Labs Bolt T-Shirt
    def Bolt_T_Shirt_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BOLT_T_SHIRT_BUTTON)).click()

    # Sauce Labs Onesie
    def onesie_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ONESIE_BUTTON)).click()

    # Перейдите в корзину
    def basket_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BASKET_BUTTON)).click()

    # Создание класса для страницы корзины,
    # который будет содержать методы для нажатия кнопки Checkout
class CartPage(ShopPage):
    CART_ITEM_NAMES = (By.CLASS_NAME, 'inventory_item_name')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def get_item_names(self):
        # Ожидаем появление хотя бы одного товара в корзине
        self.wait.until(EC.presence_of_element_located(self.CART_ITEM_NAMES))
        # Находим все элементы с названиями
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        # Возвращаем список их текстовых значений
        return [element.text for element in elements]

    def checkout_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    # Создание класса для страницы оформления заказа

    # Зполнение формы данными (имя, фамилия, почтовый индекс)
class CheckoutPage(ShopPage):
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIP_CODE_INPUT = (By.ID, 'postal-code')  # На сайте ID равен 'postal-code'
    CONTINUE_BUTTON = (By.ID, 'continue')
    TOTAL_ELEMENT = (By.CLASS_NAME, 'summary_total_label')

    def fill_checkout_form(self, first_name, last_name, zip_code):
        self.wait.until(EC.visibility_of_element_located(
            self.FIRST_NAME_INPUT)).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located(
            self.LAST_NAME_INPUT)).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located(
            self.ZIP_CODE_INPUT)).send_keys(zip_code)

    # Hажатие кнопки Continue.
    def continue_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def get_total_price_text(self):
        total = self.wait.until( EC.visibility_of_element_located(
            (self. TOTAL_ELEMENT)))

        return total.text
