import re


def validate_username(username: str):
    return re.match("^[a-zA-Z][\\w]{3,8}$", username) is not None


def validate_name(name: str):
    return re.match("^[\\w]{2,30}$", name) is not None


def validate_password(password: str):
    return re.match("^[\\w]{4,30}$", password) is not None
