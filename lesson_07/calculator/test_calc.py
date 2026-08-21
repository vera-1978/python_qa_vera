import pytest
from selenium import webdriver
from lesson_07.calculator.calc_page import CalcPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    yield driver  # Исправлено: возвращаем driver вместо browser
    driver.quit()

def test_slow_calculator(driver):
    page = CalcPage(driver)
    page.set_delay(50)  # Устанавливаем задержку калькулятора в 4 секунды
    page.click_buttons()
    page.wait_for_display_text("15")
    final_result = page.get_display_text()

    assert final_result == "15", f"Ожидался результат '15', но калькулятор показал '{final_result}'"
