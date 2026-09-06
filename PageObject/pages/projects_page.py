from selenium.webdriver.common.by import By


class ProjectsPage:
    # Добавляем или обновляем локаторы элементов
    PAGE_TITLE = (By.TAG_NAME, 'h1')  # Локатор для заголовка страницы "Проекты"
    NEW_PROJECT_BUTTON = (By.CSS_SELECTOR, '.gf-icon.gf-icon-folder')

    # Исправляем локатор для ввода, так как h1 — это заголовок текста, а не инпут!
    # Подставьте сюда реальный селектор вашего поля ввода, например (By.ID, 'name') или (By.NAME, 'title')
    PROJECT_TITLE_INPUT = (By.CSS_SELECTOR, 'input[placeholder*="название"]')

    CREATE_BUTTON = (By.CSS_SELECTOR, '.btn.btn-sm.btn-success')
    PROJECT_CARDS = (By.CSS_SELECTOR, '#projectTitle')  # Было By.ID с решеткой — исправили на CSS
    PROJECT_TITLE_IN_CARD = (By.CSS_SELECTOR, '.btn.btn-sm.btn-success')

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://gitflic.ru/project/"

    def open(self):
        self.driver.get(self.url)

    # --- ДОБАВЛЯЕМ ЭТОТ МЕТОД ---
    def get_project_title_page(self):
        """Возвращает текст главного заголовка страницы (например, 'Проекты')"""
        return self.driver.find_element(*self.PAGE_TITLE).text

    def click_new_project(self):
        self.driver.find_element(*self.NEW_PROJECT_BUTTON).click()

    def create_project(self, project_name):
        title_field = self.driver.find_element(*self.PROJECT_TITLE_INPUT)
        title_field.clear()
        title_field.send_keys(project_name)

        create_btn = self.driver.find_element(*self.CREATE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", create_btn)
        create_btn.click()

    def get_project_names(self):
        cards = self.driver.find_elements(*self.PROJECT_CARDS)
        names = []
        for card in cards:
            try:
                title_element = card.find_element(*self.PROJECT_TITLE_IN_CARD)
                names.append(title_element.text)
            except:
                continue
        return names

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class ProjectsPage:
#     # Локаторы элементов
#     NEW_PROJECT_BUTTON = (By.CSS_SELECTOR, '.gf-icon.gf-icon-folder')
#     PROJECT_TITLE_INPUT = (By.TAG_NAME, 'h1')
#     CREATE_BUTTON = (By.CSS_SELECTOR, '.btn.btn-sm.btn-success')
#     PROJECT_CARDS = (By.ID, '#projectTitle')
#     PROJECT_TITLE_IN_CARD = (By.CSS_SELECTOR, '.btn.btn-sm.btn-success')
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.url = "https://gitflic.ru/project/"
#
#     def open(self):
#         self.driver.get(self.url)
#
#     def click_new_project(self):
#         self.driver.find_element(*self.NEW_PROJECT_BUTTON).click()
#
#     def create_project(self, project_name):
#         # Заполняем название
#         title_field = self.driver.find_element(*self.PROJECT_TITLE_INPUT)
#         title_field.clear()
#         title_field.send_keys(project_name)
#
#         # Скроллим и нажимаем создать
#         create_btn = self.driver.find_element(*self.CREATE_BUTTON)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", create_btn)
#         create_btn.click()
#
#     def get_project_names(self):
#         # Получаем все карточки проектов
#         cards = self.driver.find_elements(*self.PROJECT_CARDS)
#         names = []
#
#         for card in cards:
#             try:
#                 # Ищем название внутри карточки
#                 title_element = card.find_element(*self.PROJECT_TITLE_IN_CARD)
#                 names.append(title_element.text)
#             except:
#                 continue
#
#         return names

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class ProjectsPage:
#     # Локаторы элементов
#     PROJECT_MENU = ((By.CSS_SELECTOR, '.gf-icon.gf-icon-folder'))
#     PROJECT_PAGE_TITLE = ()
#     ADD_PROJECT_BUTTON = (By.CSS_SELECTOR, '.projects-layout__action-text')
#     TITLE_PROJECT_INPUT = (By.ID, '#projectTitle')
#     CREATE_PROJECT_SUBMIT_BUTTON = (By.CSS_SELECTOR, '.btn.btn-sm.btn-success')
#     PROJECT_HEADER = (By.CSS_SELECTOR, 'h6.mb-0')
#     PROJECT_LIST = (By.CLASS_NAME, '.h3.mb-3.mt-3')
#
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.url = "https://gitflic.ru/project/"
#
#     def open(self):
#         self.driver.get(self.url)
#
#     def click_new_project(self):
#         self.driver.find_element(*self.PROJECT_MENU).click()
#
#     def create_project(self, project_name):
#         # Заполняем название
#         title_field = self.driver.find_element(*self.PROJECT_PAGE_TITLE)
#         title_field.clear()
#         title_field.send_keys(project_name)
#
#         # Скроллим и нажимаем создать
#         create_btn = self.driver.find_element(*self.ADD_PROJECT_BUTTON)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", create_btn)
#         create_btn.click()
#
#     def get_project_names(self):
#         # Получаем все карточки проектов
#         cards = self.driver.find_elements(*self.PROJECT_HEADER)
#         names = []
#
#         for card in cards:
#             try:
#                 # Ищем название внутри карточки
#                 title_element = card.find_element(*self.PROJECT_LIST)
#                 names.append(title_element.text)
#             except:
#                 continue
#
#         return names