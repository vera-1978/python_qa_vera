from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/visibility")

button_hide = driver.find_element(
    By.ID, "hideButton")
button_hide.click()

button_visibility_hidden = driver.find_element(
    By.CSS_SELECTOR, "button#invisibleButton.btn.btn-info")

if button_visibility_hidden.is_displayed():
    print("Кнопка видна")
else:
    print("Кнопка скрыта")

driver.quit()
