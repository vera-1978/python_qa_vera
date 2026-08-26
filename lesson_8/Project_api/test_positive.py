from page_project import ProjectApi


api = ProjectApi()
PROJECT_ID = "YOUGILE_PROJECT_ID"


def test_create_project_success():

    response = api.create_project(title="Первый проект")
    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data


def test_update_project():

    response = api.update_project(project_id=PROJECT_ID, title="Новое название")
    assert response.status_code == 200
    body = response.json()
    assert "id" in body


def test_get_projects():
    response = api.get_projects()
    assert response.status_code == 200
