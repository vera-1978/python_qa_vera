import pytest
from driver_factory import create_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберите браузер для тестов: chrome, firefox, safari, edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск в headless режиме (без графического интерфейса)"
    )


@pytest.fixture(scope="session")
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")

    driver = create_driver(browser_name, headless=headless_mode)

    # Максимизируем окно только если не headless режим
    if not headless_mode:
        driver.maximize_window()

    driver.get('https://gitflic.ru/')
    driver.add_cookie({
       "name": 'SESSION',
       "value": 'ZWVkZDdmMjItZWQ1MC00MWE3LWJkMDctMDdlYWM0MWI2NDUx',
       "domain": 'gitflic.ru'
    })
    driver.add_cookie({
        "name": 'cookiesAccepted',
        "value": 'true',
        "domain": 'gitflic.ru'
    })
    driver.refresh()
    yield driver
    driver.quit()