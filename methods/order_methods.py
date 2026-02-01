import requests
import allure

from data.urls import Urls


class OrderMethods:
    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload: dict, access_token: str | None = None):
        headers = {}
        if access_token:
            headers["Authorization"] = access_token
        return requests.post(Urls.CREATE_ORDER, json=payload, headers=headers)
