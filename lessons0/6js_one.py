from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ru.wikipedia.org/wiki/")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)

contact_link = driver.find_element(By.CSS_SELECTOR,
"#footer-places-contact a")
print(contact_link.get_attribute("href"))
print(contact_link.text)

contact_link.click()
sleep(5)

driver.quit()
