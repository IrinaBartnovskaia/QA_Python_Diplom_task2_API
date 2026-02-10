import pytest

from helpers import build_user_payload
from methods.user_methods import UserMethods


@pytest.fixture
def user_payload():
    return build_user_payload()


@pytest.fixture
def create_and_delete_user():
    payload = build_user_payload()
    response = UserMethods.create_user(payload)
    token = response.json().get("accessToken")

    yield payload["email"], payload["password"]

    if token:
        UserMethods.delete_user(token)
