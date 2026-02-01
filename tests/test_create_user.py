import allure
import pytest

from methods.user_methods import UserMethods
from data.message_error import MessageError


@allure.title("Создание пользователя: успех")
def test_create_user_success(user_payload):
    resp = UserMethods.create_user(user_payload)
    assert resp.status_code == 200
    assert resp.json().get("success") is True


@allure.title("Создание пользователя: без обязательных полей")
@pytest.mark.parametrize("payload", [
    {"email": "", "password": "123", "name": "A"},
    {"email": "a@b.ru", "password": "", "name": "A"},
    {"email": "a@b.ru", "password": "123", "name": ""},
])
def test_create_user_required_fields(payload):
    resp = UserMethods.create_user(payload)
    assert resp.status_code == 403
    assert resp.json().get("message") == MessageError.REQUIRED_FIELDS
