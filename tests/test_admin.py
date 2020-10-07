from unittest import TestCase
from unittest.mock import patch
from src.operations import admin_operations
from src.classes import users


class TestAdmin(TestCase):

    @patch("src.operations.bill_operations.get_bill_for_user")
    @patch("src.db_operations.users_db.check_if_username_exists")
    def test_get_user_bills(self,check_if_username_exists_mock,get_bill_for_user_mock):
        check_if_username_exists_mock.return_value = True
        get_bill_for_user_mock.return_value = ["Bill Data"]
        self.assertIsInstance(admin_operations.get_user_bills("username"), list)

    @patch("src.db_operations.users_db.check_if_username_exists")
    def test_get_user_bills_for_false(self, check_if_username_exists_mock):
        check_if_username_exists_mock.return_value = False
        self.assertFalse(admin_operations.get_user_bills("username"))

    @patch("src.operations.cart_operations.get_cart_data_to_print")
    @patch("src.db_operations.users_db.check_if_username_exists")
    def test_get_user_cart(self, check_if_username_exists_mock, get_cart_data_to_print):
        check_if_username_exists_mock.return_value = True
        get_cart_data_to_print.return_value = ["cart data"]
        self.assertEqual(admin_operations.get_user_cart("username"), get_cart_data_to_print("username"))

    @patch("src.db_operations.users_db.check_if_username_exists")
    def test_get_user_cart_for_false(self, check_if_username_exists_mock):
        check_if_username_exists_mock.return_value = False
        self.assertFalse(admin_operations.get_user_cart("username"))

    @patch("src.db_operations.categories_db.insert_new_category")
    def test_add_category(self, insert_new_category_mock):
        insert_new_category_mock.return_value = "1"
        user = users.User("username", "password", "name", 0)
        self.assertEqual(admin_operations.add_category(user, "new_category"), insert_new_category_mock("new_category"))

