import pytest
from sqlalchemy import create_engine, text


INSERT_AUTHOR_QUERY = text("""
    INSERT INTO authors (first_name, last_name, birth_year)
    VALUES (:first_name, :last_name, :birth_year)
    RETURNING author_id;
""")

UPDATE_AUTHOR_QUERY = text("""
            UPDATE authors
            SET first_name = :new_first_name,
                last_name = :new_last_name,
                birth_year = :new_birth_year
            WHERE author_id = :author_id;
        """)

SELECT_AUTHOR_QUERY = text("""
    SELECT first_name, last_name, birth_year
    FROM authors
    WHERE author_id = :author_id;
""")

DELETE_AUTHOR_QUERY = text("DELETE FROM authors WHERE author_id = :author_id;")

engine = create_engine("BASE")


@pytest.fixture
def db_author():
    first_name = 'Александр'
    last_name = 'Пушкин'
    birth_year = 1799

    with engine.connect() as connection:
        result = connection.execute(
            INSERT_AUTHOR_QUERY,
            {"first_name": first_name, "last_name": last_name,
             "birth_year": birth_year}
        )
        connection.commit()
        author_id = result.scalar()

        return author_id


def test_authors(db_author):
    # Проверяем, что ID существует
    assert db_author is not None

    # Очистка.
    with engine.connect() as connection:
        connection.execute(DELETE_AUTHOR_QUERY, {"author_id": db_author})
        connection.commit()


def test_update_author(db_author):
    # Новые данные для изменения
    new_first_name = 'Николай'
    new_last_name = 'Некрасов'
    new_birth_year = 1821

    with engine.connect() as connection:

        #  ИЗМЕНЕНИЕ АВТОРА (UPDATE)
        connection.execute(
            UPDATE_AUTHOR_QUERY,
            {
                "new_first_name": new_first_name,
                "new_last_name": new_last_name,
                "new_birth_year": new_birth_year,
                "author_id": db_author
            }
        )
        connection.commit()

        # ПРОВЕРКА ИЗМЕНЕНИЙ
        updated_author = connection.execute(
            SELECT_AUTHOR_QUERY, {"author_id": db_author}).mappings().one()

        # Проверяем, что в БД теперь лежат новые данные
        assert updated_author["first_name"] == new_first_name
        assert updated_author["last_name"] == new_last_name
        assert updated_author["birth_year"] == new_birth_year

        # Очистка.
        connection.execute(DELETE_AUTHOR_QUERY, {"author_id": db_author})
        connection.commit()


def test_delete_author_by_id():
    first_name = 'Александр'
    last_name = 'Пушкин'
    birth_year = 1799

    with engine.connect() as connection:
        result = connection.execute(
            INSERT_AUTHOR_QUERY,
            {"first_name": first_name, "last_name": last_name, "birth_year": birth_year}
        )
        connection.commit()

        # Получаем ID.
        target_id = result.scalar()
        assert target_id is not None  # Убеждаемся, что ID создался

        # Очистка.
        connection.execute(DELETE_AUTHOR_QUERY,
                           {"author_id": target_id})
        connection.commit()

        # Проверяем, что автора больше нет в БД
        check_deleted = connection.execute(
            SELECT_AUTHOR_QUERY, {"author_id": target_id}).fetchone()
        assert check_deleted is None
