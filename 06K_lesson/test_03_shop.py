from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    # Инициализируем драйвер (не перезаписываем переданный аргумент)
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    # Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
    driver.get('https://www.saucedemo.com/')

    # Авторизуйтесь как пользователь standard_user
    input_username = driver.find_element(By.ID, 'user-name')
    input_username.send_keys('standard_user')

    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    # Добавьте в корзину товары:
    # Sauce Labs Backpack
    Backpack_button = wait.until(
        EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))
    )
    Backpack_button.click()

    # Sauce Labs Bolt T-Shirt
    Bolt_T_Shirt_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'))
    )
    Bolt_T_Shirt_button.click()

    # Sauce Labs Onesie
    onesie_button = wait.until(
        EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-onesie'))
    )
    onesie_button.click()

    # Перейдите в корзину
    basket_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))
    )
    basket_button.click()

    # Нажмите Checkout
    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, 'checkout'))
    )
    checkout_button.click()

    # Заполните форму своими данными:
    # имя
    input_first_name = driver.find_element(By.ID, 'first-name')
    input_first_name.send_keys('Vera')

    # фамилия
    input_last_name = driver.find_element(By.ID, 'last-name')
    input_last_name.send_keys('Ivanova')

    # почтовый индекс
    input_zip = driver.find_element(By.ID, 'postal-code')
    input_zip.send_keys('424910')

    # Нажмите кнопку Continue
    continue_button = wait.until(
        EC.element_to_be_clickable((By.ID, 'continue'))
    )
    continue_button.click()

    # Прочитайте со страницы итоговую стоимость ( Total )
    total_element = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, 'summary_total_label'))
    )
    total_text = total_element.text  # Текст имеет вид "Total: $58.29"

    # Закройте браузер
    driver.quit()

    # Проверьте, что итоговая сумма равна $58.29
    assert total_text == 'Total: $58.29', (f"Ожидалось Total: "
                                           f"$58.29, получено {total_text}")
