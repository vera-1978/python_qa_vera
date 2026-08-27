from page_project import ProjectApi


api = ProjectApi()
PROJECT_ID = "33c7e041-f93a-42fe-9801-73062e02b980"


def test_create_project_success():
    response = api.create_project(title="Первый проект")
    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data


def test_update_project():
    response = api.create_project(title="Первый проект")
    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data

    response = api.update_project(project_id=PROJECT_ID, title="Новое название")
    assert response.status_code == 200
    body = response.json()
    assert "id" in body


def test_get_projects():
    response = api.create_project(title="Первый проект")
    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data

    response = api.get_projects()
    assert response.status_code == 200
