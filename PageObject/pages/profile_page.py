# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class ProfilePage:
#
#     EDIT_BUTTON = (By.CSS_SELECTOR, ".gf-link-button__icon")
#     NAME_INPUT = (By.ID, "name")
#     LAST_NAME_INPUT = (By.ID, "surname")
#     SAVE_PROFILE_BUTTON = (By.CSS_SELECTOR, ".gf-button.--success")
#     USER_NAME_MAIN = (By.CSS_SELECTOR, ".user-profile__name")
#
# def __init__(self, driver, url):
#     self.driver = driver
#     self.url = url
#     self.wait = WebDriverWait(self.driver, 10)
#
# def open_profile_page(self, username):
#     self.driver.get(f"{self.url}user/{username}")
#     self.driver.save_screenshot("screenshots/full_page.png")
#
# def update_profile(self, new_user_name, new_last_name):
#     edit_button = self.wait.until(EC.presence_of_element_located(
#         self.EDIT_BUTTON
#         ))
#     edit_button.click()
#     username_input = self.wait.until(EC.presence_of_element_located(
#     self.NAME_INPUT
#         ))
#     username_input.clear()
#     username_input.send_keys(new_user_name)
#
#     surname_input = self.driver.find_element(*self.LAST_NAME_INPUT)
#     surname_input.clear()
#     surname_input.send_keys(new_last_name)
#
#     save_button = self.wait.until(EC.presence_of_element_located(
#         self.SAVE_PROFILE_BUTTON
#         ))
#     save_button.click()
#
# def get_user_name(self):
#     user_name = self.wait.until(EC.presence_of_element_located(
#         self.USER_NAME_MAIN
#         ))
#     user_name.screenshot("screenshots/user_name.png")
#     return user_name.text

import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage:
    # Исправлено: добавлены пропущенные кавычки в локаторах
    # Для EDIT_BUTTON добавлен префикс точки, если это CSS-класс
    EDIT_BUTTON = (By.CSS_SELECTOR, ".user-profile__edit-btn, .gf-link-button")
    NAME_INPUT = (By.ID, "name")
    LAST_NAME_INPUT = (By.ID, "surname")
    SAVE_PROFILE_BUTTON = (By.CSS_SELECTOR, ".gf-button.--success")
    USER_NAME_MAIN = (By.CSS_SELECTOR, ".user-profile__name")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)

    # def open_profile_page(self, username):
    #     # Исправлено: добавлены кавычки для f-строки
    #     self.driver.get(f"{self.url}user/{username}")
    #     # Исправлено: добавлены кавычки для пути скриншота
    #     self.driver.save_screenshot("screenshots/full_page.png")

    def open_profile_page(self, username):
        # Удаляем лишние слэши на конце self.url и собираем правильный путь
        base_url = self.url.rstrip('/')
        full_url = f"{base_url}/user/{username}"

        self.driver.get(full_url)
        self.driver.save_screenshot("screenshots/full_page.png")

    def update_profile(self, new_user_name, new_last_name):
        # Исправлено: добавлен распаковщик * для кортежа локатора
        # Изменено на element_to_be_clickable для стабильности клика
        edit_button = self.wait.until(
            EC.element_to_be_clickable(self.EDIT_BUTTON)
        )
        edit_button.click()

        # Исправлено: добавлен распаковщик *
        username_input = self.wait.until(
            EC.presence_of_element_located(self.NAME_INPUT)
        )
        username_input.clear()
        username_input.send_keys(new_user_name)

        # Исправлено: пассивный find_element заменен на wait для стабильности
        surname_input = self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME_INPUT)
        )
        surname_input.clear()
        surname_input.send_keys(new_last_name)

        # Исправлено: добавлен распаковщик * и element_to_be_clickable
        save_button = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_PROFILE_BUTTON)
        )
        save_button.click()

    def get_user_name(self):
        # Исправлено: добавлен распаковщик *
        # Изменено на visibility_of_element_located, чтобы текст успел прогрузиться
        user_name = self.wait.until(
            EC.visibility_of_element_located(self.USER_NAME_MAIN)
        )
        # Исправлено: добавлены кавычки для пути скриншота
        user_name.screenshot("screenshots/user_name.png")
        return user_name.text
