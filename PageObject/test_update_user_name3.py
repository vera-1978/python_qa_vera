from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
fake = Faker()


def open_profile_page(driver):
    driver.get("https://gitflic.ru/user/arkadwera")
    driver.save_screenshot("screenshots/full_page.png")


def update_profile(driver, wait, nev_user_name, nev_last_name):
    # 3. Ожидаем кликабельности и нажимаем кнопку редактирования профиля
    edit_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "gf-link-button__icon")))
    edit_button.click()
    # 4. Заполняем поле "Имя"
    username_input = wait.until(
        EC.visibility_of_element_located((By.ID, "name")))
    username_input.clear()
    username_input.send_keys(nev_user_name)

    # 5. Заполняем поле "Фамилия" (теперь тоже с безопасным ожиданием)
    surname_input = wait.until(
        EC.visibility_of_element_located((By.ID, "surname")))
    surname_input.clear()
    surname_input.send_keys(nev_last_name)

    # 6. Нажимаем кнопку сохранения изменений
    save_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".gf-button.--success")))
    save_button.click()


def get_user_name(wait):
    # 8. Проверяем, что Ф и И успешно отображаются на странице
    user_name = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".user-profile__name")))
    user_name.screenshot("screenshots/user_name.png")
    return user_name.text


def test_update_user_name(driver):
    wait = WebDriverWait(driver, 20)
    open_profile_page(driver)

    user_name = Faker().first_name()
    last_name = Faker().last_name()
    update_profile(driver, wait, user_name, last_name)

    # 7. Возвращаемся на страницу ТОГО ЖЕ профиля (arkadwera)
    open_profile_page(driver)

    assert get_user_name(wait) == user_name + ' ' + last_name
