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
    assert response.status_code == 201
    response_data = response.json()
    # Проверяем, что ID не создался
    assert "id" in response_data


# Негативный сценарий: в верхней части файла объявлена константа
# заглавными буквами (API_TOKEN), а внутри теста написана строчными (api_token).
def test_update_project():
    url = f"{URL}/{PROJECT_ID}"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    payload = {"title": "Новое название"}
    resp = requests.put(url, headers=headers, json=payload)
    body = resp.json()

    assert resp.status_code == 200
    assert "id" in body


    # Негативный сценарий: отправляем пустые заголовки без поля Authorization
def test_get_projects():
    headers = {
                # "Authorization": f"Bearer {API_TOKEN}",
                "Content-Type": "application/json",
            }
    resp = requests.get(URL, headers=headers)

    assert resp.status_code == 200
