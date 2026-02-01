import pytest

from data.generators import random_email, random_password, random_name
from methods.user_methods import UserMethods


@pytest.fixture
def user_payload():
    """
    Данные для создания пользователя
    Используется в test_create_user.py и test_auth_user.py
    """
    return {
        "email": random_email(),
        "password": random_password(),
        "name": random_name()
    }


@pytest.fixture
def create_and_delete_user():
    """
    Фикстура для тестов заказов
    Возвращает (email, password)
    """
    payload = {
        "email": random_email(),
        "password": random_password(),
        "name": random_name()
    }

    # создаём пользователя
    response = UserMethods.create_user(payload)
    token = response.json().get("accessToken")

    # отдаём email и пароль (КАК ОЖИДАЮТ ТЕСТЫ)
    yield payload["email"], payload["password"]

    # удаляем пользователя после теста
    if token:
        UserMethods.delete_user(token)
