from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

driver.get("http://uitestingplayground.com/animation")

grey_button = wait.until(
   EC.presence_of_element_located((By.ID, "animationButton"))
)
grey_button.click()
sleep(2)

blue_button = driver.find_element(By.ID, "movingTarget")
driver.execute_script("arguments[0].click();", blue_button)
sleep(3)

driver.quit()