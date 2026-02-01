from uuid import uuid4


def random_email() -> str:
    return f"ira_{uuid4().hex[:10]}@example.com"


def random_password() -> str:
    return f"Pass_{uuid4().hex[:10]}"


def random_name() -> str:
    return f"User_{uuid4().hex[:8]}"
