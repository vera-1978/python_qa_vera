import requests


API_TOKEN = "YOUGILE_TOKEN"
URL = "https://ru.yougile.com/api-v2/projects"
PROJECT_ID = "YOUGILE_PROJECT_ID"


def test_create_project_success():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    # Негативный сценарий: передаем пустое название
    payload = {"title": ""}

    response = requests.post(URL, json=payload, headers=headers)

    # Проверяем, что сервер вернул ошибку 400
    assert response.status_code == 400


def test_update_project():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {"title": "Первый проект"}

    response = requests.post(URL, json=payload, headers=headers)

    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data

    # Негативный сценарий: в верхней части файла объявлена константа
    # заглавными буквами (API_TOKEN), а внутри теста написана строчными (api_token).
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    url = f"{URL}/{PROJECT_ID}"

    payload = {"title": "Новое название"}
    resp = requests.put(url, headers=headers, json=payload)

    assert resp.status_code == 401


def test_get_projects():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {"title": "Первый проект"}
    response = requests.post(URL, json=payload, headers=headers)

    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data

    # Негативный сценарий: отправляем пустые заголовки без поля Authorization
    headers = {
        # "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }
    resp = requests.get(URL, headers=headers)

    assert resp.status_code == 401
