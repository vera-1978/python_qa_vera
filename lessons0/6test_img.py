from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_image_loading():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждем завершения загрузки
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

    # Находим все изображения
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

    # Проверяем изображения
    assert len(images) == 4

    expected_files = [
        "compass.png",
        "calendar.png",
        "award.png",
        "landscape.png"
    ]

    for i, img in enumerate(images):
        src = img.get_attribute("src")
        assert expected_files[i] in src
        assert img.is_displayed()

    driver.quit()
