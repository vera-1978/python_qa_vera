import allure
import pytest
from selenium import webdriver
from calc_page import CalcPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    yield driver
    driver.quit()


@allure.title("Проверка функциональности калькулятора")
@allure.description("Тест проверяет сложение 7 + 8 с задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(driver):
    with allure.step('Инициализация страницы калькулятора'):
        page = CalcPage(driver)

    with allure.step('Ввести значение 45 в поле задержки'):
        page.set_delay(50)

    with allure.step('Нажать кнопки: 7, +, 8, ='):
        page.click_buttons()

    with allure.step('Ожидать отображения результата "15"'):
        page.wait_for_display_text("15")

    with allure.step('Получить итоговый результат с экрана'):
        final_result = page.get_display_text()

    with allure.step('Проверить, что в окне отобразится результат 15'):
        assert final_result == "15"
