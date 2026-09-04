import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Получаем значение переменной
database_url = os.getenv("DATABASE_URL")

print(f"Адрес базы данных: {database_url}")

