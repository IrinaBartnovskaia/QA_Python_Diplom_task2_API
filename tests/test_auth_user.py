import allure

from methods.user_methods import UserMethods
from data.message_error import MessageError


@allure.epic("User")
@allure.feature("Authorization")
class TestAuthUser:

    @allure.title("Авторизация пользователя: успех")
    def test_login_success(self, user_payload):
        UserMethods.create_user(user_payload)
        resp = UserMethods.login(
            {
                "email": user_payload["email"],
                "password": user_payload["password"],
            }
        )

        assert resp.status_code == 200
        assert resp.json().get("success") is True

    @allure.title("Авторизация пользователя: неверные данные")
    def test_login_incorrect_data(self):
        resp = UserMethods.login(
            {
                "email": "nope@example.com",
                "password": "wrong",
            }
        )
        assert resp.status_code == 401
        assert resp.json().get("message") == MessageError.INCORRECT_DATA
