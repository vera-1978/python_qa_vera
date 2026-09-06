from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/disabledinput")
driver.maximize_window()

# driver.find_element(By.ID, "enableButton").click()

input_element = driver.find_element(By.ID, "inputField")

if input_element.is_enabled():
    print("Input element is enabled")
else:
    print("Input element is blocked")

driver.quit()