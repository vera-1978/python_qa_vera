from sys import maxsize
from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://gitflic.ru/')


driver.add_cookie({
    'name': 'SESSION',
    'value': 'NDVmOTRiM2MtNTA3ZC00NzQ1LWExNTctMTRkZGI4MDg0YzJk',
    'domain': 'gitflic.ru'
})

driver.add_cookie({
    'name': 'cookiesAccepted',
    'value': 'true',
    'domain': 'gitflic.ru'
})

driver.refresh()
driver.get('https://gitflic.ru/user/arkadwera')

sleep(5)

driver. delete_all_cookies()
driver.refresh()
sleep(5)

driver.quit()
