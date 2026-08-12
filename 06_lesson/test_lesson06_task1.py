from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    # 2. Найдите и нажмите на кнопку "Start"
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    # 3. Дождитесь появления текста "Hello World!"
    # Используем WebDriverWait для явного ожидания до 10 секунд
    wait = WebDriverWait(driver, 10)
    hello_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish")))

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshots/whole_page.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert hello_element.text == "Hello World!"

    driver.quit()
