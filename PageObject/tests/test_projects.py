from  PageObject.pages.projects_page import ProjectsPage
import faker


def test_create_and_check_project(driver_authorized):
    # Передаем правильное имя фикстуры, которую запросили в тесте
    projects_page = ProjectsPage(driver_authorized)



    # Проверяем
    assert projects_page.get_project_title_page() == 'Платформа для работы с кодом'