import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Получаем значение переменной
database_url = os.getenv("DATABASEQA")

print(f"Адрес базы данных: {database_url}")

