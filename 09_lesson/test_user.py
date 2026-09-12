import os
import pytest
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("DATABASEQA")
engine = create_engine(database_url)


@pytest.fixture
def db_user():
    user_email = 'new_calculated_user@example.com'
    subject_id = 10

    with engine.connect() as connection:
        query = text("""
            INSERT INTO public.users (user_id, user_email, subject_id)
            VALUES (
                (SELECT COALESCE(MAX(user_id), 0) + 1 FROM public.users),
                :user_email,
                :subject_id
            )
            RETURNING user_id;
        """)
        result = connection.execute(
            query, {"user_email": user_email, "subject_id": subject_id})
        connection.commit()
        new_user_id = result.scalar()

        # Проверка, что пользователь успешно создан
        assert new_user_id

        return new_user_id


def test_insert_user(db_user):
    with engine.connect() as connection:
        #  Проверка только что добавленного пользователя
        select_query = text("""
            SELECT user_id, user_email, subject_id
            FROM public.users
            WHERE user_id = :user_id;
        """)
        new_user_id = connection.execute(
            select_query, {"user_id": db_user}).fetchone()
        assert new_user_id

        # Очистка: удаляем созданного пользователя
        delete_query = text(
            "DELETE FROM public.users WHERE user_id = :user_id;")
        connection.execute(delete_query, {"user_id": db_user})
        connection.commit()


def test_update_user(db_user):
    new_subject_id = 8

    with engine.connect() as connection:
        # Обновляем subject_id
        update_query = text("""
            UPDATE public.users
            SET subject_id = :new_subject_id
            WHERE user_id = :user_id;
        """)

        connection.execute(
            update_query,
            {"new_subject_id": new_subject_id, "user_id": db_user}
        )
        connection.commit()

        # Запрашиваем измененные данные для проверки
        select_query = text("""
            SELECT user_id, user_email, subject_id
            FROM public.users
            WHERE user_id = :user_id;
        """)
        user_row = connection.execute(
            select_query, {"user_id": db_user}).fetchone()

        # Проверяем, что изменения применились корректно
        assert user_row.subject_id == new_subject_id

        # Очистка
        delete_query = text(
            "DELETE FROM public.users WHERE user_id = :user_id;")
        connection.execute(delete_query, {"user_id": db_user})
        connection.commit()


def test_delete_user():
    user_email = 'new_calculated_user@example.com'
    subject_id = 10

    with engine.connect() as connection:
        query = text("""
            INSERT INTO public.users (user_id, user_email, subject_id)
            VALUES (
                (SELECT COALESCE(MAX(user_id), 0) + 1 FROM public.users),
                :user_email,
                :subject_id
            )
            RETURNING user_id;
        """)
        result = connection.execute(
            query, {"user_email": user_email, "subject_id": subject_id})
        connection.commit()
        new_user_id = result.scalar()

        assert new_user_id
        # Очистка: удаляем созданного пользователя
        delete_query = text(
            "DELETE FROM public.users WHERE user_id = :user_id;")
        connection.execute(delete_query, {"user_id": new_user_id})
        connection.commit()
        # Проверяем, что автора больше нет в БД
        select_query = text("""
            SELECT * FROM public.users WHERE user_id = :user_id;
        """)

        # Выполняем запрос и сохраняем результат в переменную user_row
        user_row = connection.execute(
            select_query, {"user_id": new_user_id}).fetchone()

        assert user_row is None
