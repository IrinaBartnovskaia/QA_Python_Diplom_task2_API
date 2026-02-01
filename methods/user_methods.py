import requests
import allure

from data.urls import Urls


class UserMethods:
    @staticmethod
    @allure.step("Создать пользователя")
    def create_user(payload: dict):
        return requests.post(Urls.CREATE_USER, json=payload)

    @staticmethod
    @allure.step("Авторизовать пользователя")
    def login(payload: dict):
        return requests.post(Urls.AUTH_USER, json=payload)

    @staticmethod
    @allure.step("Авторизовать пользователя (email, password)")
    def login_user(email: str, password: str):
        """
        НУЖНО для тестов, которые вызывают UserMethods.login_user(email, password)
        Возвращает response.
        """
        return requests.post(Urls.AUTH_USER, json={"email": email, "password": password})

    @staticmethod
    @allure.step("Удалить пользователя")
    def delete_user(access_token: str):
        headers = {"Authorization": access_token}
        return requests.delete(Urls.DELETE_USER, headers=headers)
