from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form(driver):
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    # Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    # в Edge или Safari
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    # Заполните форму значениями:
    # First name  Иван
    first_name_input = wait.until(
        EC.element_to_be_clickable((By.NAME, 'first-name')))
    first_name_input.send_keys('Иван')

    # Last name Петров
    Last_name_input = wait.until(
        EC.element_to_be_clickable((By.NAME, 'last-name')))
    Last_name_input.send_keys('Петров')

    # Address Ленина, 55-3
    Address_input = wait.until(
        EC.element_to_be_clickable((By.NAME, 'address')))
    Address_input.send_keys('Ленина, 55-3')

    # Email test@skypro.com
    Email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'e-mail')))
    Email_input.send_keys('test@skypro.com')

    # Phone number +7985899998787
    Phone_number_input = wait.until(
        EC.element_to_be_clickable((By.NAME, 'phone')))
    Phone_number_input.send_keys('+7985899998787')

    # Zip code *оставить пустым
    Zip_code_input = wait.until(
        EC.element_to_be_clickable((By.NAME, 'zip-code')))

    # City Москва
    City_input = wait.until(EC.element_to_be_clickable((By.NAME, 'city')))
    City_input.send_keys('Москва')

    # Country Россия
    Country_input = wait.until(
        EC.element_to_be_clickable((By.NAME, 'country')))
    Country_input.send_keys('Россия')

    # Job position  QA
    Job_position_input = wait.until(
        EC.element_to_be_clickable((By.NAME, 'job-position')))
    Job_position_input.send_keys('QA')

    # Company SkyPro
    Company_input = wait.until(
        EC.element_to_be_clickable((By.NAME, 'company')))
    Company_input.send_keys('SkyPro')

    # Нажмите кнопку Submit.
    Submit_button = driver.find_element(
        By.CSS_SELECTOR, '.btn.btn-outline-primary')
    Submit_button.click()
    driver.save_screenshot("screenshots/whole_page.png")
    # # Проверьте ( assert ), что поле Zip code подсвечено красным.
    zip_class = driver.find_element(By.ID, 'zip-code').get_attribute("class")
    assert "alert-danger" in zip_class
    # Проверьте ( assert ), что остальные поля подсвечены зеленым.
    fields_to_check = [
        'first-name', 'last-name', 'address', 'e-mail',
        'phone', 'city', 'country', 'job-position', 'company'
    ]

    for field_name in fields_to_check:
        field = driver.find_element(By.ID, field_name)
        assert "alert-success" in field.get_attribute(
            "class"), f"Поле {field_name} должно быть зеленым!"

    driver.quit()
