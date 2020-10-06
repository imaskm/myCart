from src.custom_exceptions import users_exceptions
from src.validations import validate_users


class User:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, username, password, name, is_admin=0):
        self.username = username
        self.password = password
        self.name = name
        self.is_admin = is_admin

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username: str):
        if not validate_users.validate_username(username):
            raise users_exceptions.InvalidUsernameException
        self._username = username

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not validate_users.validate_name(name):
            raise users_exceptions.InvalidNameException
        self._name = name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if not validate_users.validate_password(password):
            raise users_exceptions.InvalidPasswordException
        self._password = password

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        if value not in [0,1]:
            raise ValueError("is_admin can contain either 0 or 1")
        self._is_admin = value


