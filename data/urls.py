class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"

    # user
    CREATE_USER = f"{BASE_URL}/api/auth/register"
    AUTH_USER = f"{BASE_URL}/api/auth/login"
    DELETE_USER = f"{BASE_URL}/api/auth/user"

    # orders
    CREATE_ORDER = f"{BASE_URL}/api/orders"
    INGREDIENTS = f"{BASE_URL}/api/ingredients"

