from unittest import TestCase
from unittest.mock import patch
from src.classes import users
from src.operations import users_operations
from src.validations import validate_users
from src.custom_exceptions import users_exceptions


class TestUser(TestCase):

    def test_object_creation(self):
        user = users.User("username", "password", "name", 0)
        self.assertIsInstance(user, users.User)

    def test_object_creation_exceptions(self):
        self.assertRaises(users_exceptions.InvalidUsernameException, users.User, "u", "password", "name")
        self.assertRaises(users_exceptions.InvalidPasswordException, users.User, "username", "pw", "name")
        self.assertRaises(users_exceptions.InvalidNameException, users.User, "username", "password", "n", 0)
        self.assertRaises(ValueError, users.User, "username", "password", "name", 12)

    @patch('src.db_operations.users_db.update_users_active_cart')
    @patch('src.operations.products_operations.get_product_details_if_can_be_added')
    def test_add_product_to_users_cart(self, get_product_details_if_can_be_added_mock, update_users_active_cart_mock):
        get_product_details_if_can_be_added_mock.return_value = True
        update_users_active_cart_mock.return_value = True
        result = users_operations.add_product_to_users_cart(users.User, 1, 1)
        self.assertEqual(result, True)

    def test_validate_users_validate_username_false(self):
        result = validate_users.validate_username("tes")
        self.assertEqual(result, False)

    def test_validate_users_validate_username_true(self):
        result = validate_users.validate_username("testuser")
        self.assertEqual(result, True)

    def test_validate_users_validate_password_true(self):
        result = validate_users.validate_password("testpwd")
        self.assertEqual(result, True)

    def test_validate_users_validate_password_false(self):
        result = validate_users.validate_password("pwd")
        self.assertEqual(result, False)

    def test_validate_users_validate_name_true(self):
        result = validate_users.validate_username("testname")
        self.assertEqual(result, True)

    def test_validate_users_validate_name_false(self):
        result = validate_users.validate_username("I")
        self.assertEqual(result, False)
