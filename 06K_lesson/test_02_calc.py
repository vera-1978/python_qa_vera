from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_02_calc():
    # Инициализируем драйвер (не перезаписываем переданный аргумент)
    driver = webdriver.Chrome()

    # Шаг 1: Открыть страницу калькулятора
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    # Шаг 2: В поле ввода #delay ввести значение 45
    # (Используем локатор CSS для ID, это быстрее и лаконичнее)
    delay_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#delay'))
    )
    delay_input.clear()
    delay_input.send_keys('45')
    # Нажмите на кнопки:
    # 7
    driver.find_element(
        By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']").click()
    # # +
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    # 8
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    # =
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-warning').click()

    # Ждем появления результата '15' на экране в течение 50 секунд (с запасом)
    display_locator = (By.CSS_SELECTOR, ".screen")

    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element(display_locator, "15")
    )

    result_text = driver.find_element(*display_locator).text
    assert (
            result_text == "15"
    ), f"Ожидался результат '15', но получили '{result_text}'"

    driver.quit()
