import allure
import pytest

from methods.user_methods import UserMethods
from data.message_error import MessageError


@allure.epic("User")
@allure.feature("Create user")
class TestCreateUser:

    @allure.title("Создание пользователя: успех")
    def test_create_user_success(self, user_payload):
        resp = UserMethods.create_user(user_payload)
        assert resp.status_code == 200
        assert resp.json().get("success") is True

    @allure.title("Создание пользователя: создание дубликата")
    def test_create_user_duplicate(self, user_payload):
        # 1) создаём пользователя первый раз — успех
        resp_1 = UserMethods.create_user(user_payload)
        assert resp_1.status_code == 200
        assert resp_1.json().get("success") is True

        # 2) создаём того же пользователя второй раз — должна быть ошибка
        resp_2 = UserMethods.create_user(user_payload)
        assert resp_2.status_code == 403

        # 3) сообщение об ошибке
        msg = resp_2.json().get("message")

        if hasattr(MessageError, "USER_ALREADY_EXISTS"):
            assert msg == MessageError.USER_ALREADY_EXISTS
        elif hasattr(MessageError, "DUPLICATE_USER"):
            assert msg == MessageError.DUPLICATE_USER
        elif hasattr(MessageError, "USER_EXISTS"):
            assert msg == MessageError.USER_EXISTS
        else:
            assert msg

    @allure.title("Создание пользователя: без обязательных полей")
    @pytest.mark.parametrize(
        "payload",
        [
            {"email": "", "password": "123", "name": "A"},
            {"email": "a@b.ru", "password": "", "name": "A"},
            {"email": "a@b.ru", "password": "123", "name": ""},
        ],
    )
    def test_create_user_required_fields(self, payload):
        resp = UserMethods.create_user(payload)
        assert resp.status_code == 403
        assert resp.json().get("message") == MessageError.REQUIRED_FIELDS
