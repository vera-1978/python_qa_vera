import requests

# Применение паттерна PageObject для позитивного теста.
class ProjectApi:
    def __init__(self):
        self.url = "https://ru.yougile.com/api-v2/projects"
        self.token = "YOUGILE_TOKEN"

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str):
        payload = {"title": title}
        return requests.post(self.url, json=payload, headers=self.headers)

    def update_project(self, project_id: str, title: str):
        url = f"{self.url}/{project_id}" if project_id else self.url
        payload = {"title": title}
        return requests.put(url, json=payload, headers=self.headers)

    def get_projects(self):
        return requests.get(self.url, headers=self.headers)
