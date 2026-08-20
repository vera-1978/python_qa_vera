from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


def test_open_google():
    # Настраиваем службу и указываем наш файл драйвера
    service = Service(executable_path="geckodriver.exe")

    # Запускаем браузер Firefox
    driver = webdriver.Firefox(service=service)

    # Открываем сайт
    driver.get("https://google.com")

    # Небольшая пауза, чтобы успеть увидеть браузер
    time.sleep(3)

    # Обязательно закрываем браузер в конце теста
    driver.quit()

