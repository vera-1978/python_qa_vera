# Создано два аккаунта на https://gitflic.ru/.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    # Откройте страницу https://gitflic.ru/.
    driver.get('https://gitflic.ru/')
    # Установите cookie пользователя 1.
    driver.add_cookie({
        'name': 'SESSION',
        'value': 'YmY5YzIwNWUtYzhjNC00NDY5LTkxOGEtN2M4NDFmOGI3YjMw',
        'domain': 'gitflic.ru'
    })
    # Обновите страницу.
    driver.refresh()
    # Перейдите на страницу пользователя 1.

    driver.get('https://gitflic.ru/user/arkadwera')
    # Сохраните текущий URL.
    url_user_1 = driver.current_url
    # Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.refresh()

    # Установите cookie пользователя 2.
    driver.add_cookie({
        'name': 'X-CSRF-TOKEN',
        'value': '82622639-9f07-4043-8e3f-8ffea61b50a5',
        'domain': 'gitflic.ru'
    })
    # Обновите страницу.
    driver.refresh()
    # Перейдите на страницу пользователя 2.

    driver.get('https://gitflic.ru/user/ivanova')
    # Сохраните текущий URL.
    url_user_2 = driver.current_url
    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user_1 != url_user_2, f"URL совпадают: {url_user_1}"
    print("Тест успешно пройден! URL пользователей различаются.")

    driver.quit()
