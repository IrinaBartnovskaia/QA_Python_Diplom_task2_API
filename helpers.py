from data.generators import random_email, random_password, random_name


def build_user_payload():
    return {
        "email": random_email(),
        "password": random_password(),
        "name": random_name(),
    }
