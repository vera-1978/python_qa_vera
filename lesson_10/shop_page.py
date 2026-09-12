from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


class StandardPage(ShopPage):
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя на странице логина.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль пользователя.
        """
        self.wait.until(EC.visibility_of_element_located(
            self.INPUT_USERNAME)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(
            self.INPUT_PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()


class InventoryPage(ShopPage):
    BACKPACK_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BOLT_T_SHIRT_BUTTON = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ONESIE_BUTTON = (By.ID, 'add-to-cart-sauce-labs-onesie')
    BASKET_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')

    def Backpack_button(self) -> None:
        """
        Добавляет рюкзак (Sauce Labs Backpack) в корзину.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_BUTTON)).click()

    def Bolt_T_Shirt_button(self) -> None:
        """
        Добавляет футболку (Sauce Labs Bolt T-Shirt) в корзину.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.BOLT_T_SHIRT_BUTTON)).click()

    def onesie_button(self) -> None:
        """
        Добавляет комбинезон (Sauce Labs Onesie) в корзину.
        """
        self.wait.until(EC.element_to_be_clickable(self.ONESIE_BUTTON)).click()

    def basket_button(self) -> None:
        """
        Выполняет переход на страницу корзины.
        """
        self.wait.until(EC.element_to_be_clickable(self.BASKET_BUTTON)).click()


class CartPage(ShopPage):
    CART_ITEM_NAMES = (By.CLASS_NAME, 'inventory_item_name')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def get_item_names(self) -> list[str]:
        """
        Получает названия всех товаров, находящихся в корзине.

        Returns:
            list[str]: Список с текстовыми названиями товаров.
        """
        self.wait.until(EC.presence_of_element_located(self.CART_ITEM_NAMES))
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [element.text for element in elements]

    def checkout_button(self) -> None:
        """
        Нажимает кнопку переходу к оформлению заказа (Checkout).
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()


class CheckoutPage(ShopPage):
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIP_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    TOTAL_ELEMENT = (By.CLASS_NAME, 'summary_total_label')

    def fill_checkout_form(self, first_name: str, last_name: str, zip_code: str | int) -> None:
        """
        Заполняет форму оформления заказа персональными данными.

        Args:
            first_name (str): Имя покупателя.
            last_name (str): Фамилия покупателя.
            zip_code (str | int): Почтовый индекс.
        """
        self.wait.until(EC.visibility_of_element_located(
            self.FIRST_NAME_INPUT)).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located(
            self.LAST_NAME_INPUT)).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located(
            self.ZIP_CODE_INPUT)).send_keys(str(zip_code))

    def continue_button(self) -> None:
        """
        Нажимает кнопку Continue для подтверждения введенных данных.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def get_total_price_text(self) -> str:
        """
        Получает итоговую стоимость заказа в виде текста с экрана.

        Returns:
            str: Строка с текстом полной стоимости (например, 'Total: $43.18').
        """
        total = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_ELEMENT)
        )
        return total.text

