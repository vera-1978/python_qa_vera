from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    DELAY_INPUT = (By.CSS_SELECTOR, '#delay')
    BUTTON_7 = (By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUALS = (By.CSS_SELECTOR, '.btn.btn-outline-warning')
    DISPLAY = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.short_wait = WebDriverWait(driver, 10)
        self.long_wait = WebDriverWait(driver, 50)

    def set_delay(self, delay_value):
        delay_input = self.short_wait.until(EC.element_to_be_clickable(self.DELAY_INPUT))
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_buttons(self):
        self.driver.find_element(*self.BUTTON_7).click()
        self.driver.find_element(*self.BUTTON_PLUS).click()
        self.driver.find_element(*self.BUTTON_8).click()
        self.driver.find_element(*self.BUTTON_EQUALS).click()

    def wait_for_display_text(self, text):
        """Ожидает, пока в поле дисплея появится указанный текст."""
        return self.long_wait.until(EC.text_to_be_present_in_element(self.DISPLAY, text))

    def get_display_text(self):
        """Возвращает текущее текстовое значение экрана."""
        return self.driver.find_element(*self.DISPLAY).text
