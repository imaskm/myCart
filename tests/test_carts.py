import unittest
from unittest.mock import patch
from src.classes import cartdetails, users
from src.operations import cart_operations


class TestCarts(unittest.TestCase):

    def test_object_creation(self):
        self.assertIsInstance(cartdetails.CartDetails("id", "1", "1", 1), cartdetails.CartDetails)

    @patch("src.db_operations.cart_db.get_cartdetails_from_id")
    def test_get_data_from_cart_ids(self, get_cartdetails_from_id_mock):
        get_cartdetails_from_id_mock.return_value = [["1", "1", "1", 1]]
        self.assertIsInstance(cart_operations.get_data_from_cart_ids([1]), list)

    @patch("src.db_operations.cart_db.get_cartdetails_from_id")
    def test_get_data_from_cart_ids_none(self, get_cartdetails_from_id_mock):
        get_cartdetails_from_id_mock.return_value = []
        self.assertIsNone(cart_operations.get_data_from_cart_ids([1]))
        self.assertIsNone(cart_operations.get_data_from_cart_ids([]))

    @patch("src.db_operations.cart_db.remove_product_from_cart")
    @patch("src.db_operations.cart_db.get_cartdetails_from_id")
    @patch("src.db_operations.cart_db.get_active_cart_id_for_user")
    def test_remove_product_from_cart(
            self,
            get_active_cart_id_for_user_mock,
            get_cartdetails_from_id_mock,
            remove_product_from_cart_mock
    ):
        get_active_cart_id_for_user_mock.return_value = 1
        get_cartdetails_from_id_mock.return_value = [["1", "1", "1", 2]]
        user = users.User("username","password", "name")
        remove_product_from_cart_mock.return_value = True

        self.assertTrue(cart_operations.remove_product_from_cart(user,"1"))

    @patch("src.db_operations.cart_db.remove_product_from_cart")
    @patch("src.db_operations.cart_db.get_cartdetails_from_id")
    @patch("src.db_operations.cart_db.get_active_cart_id_for_user")
    def test_remove_product_from_cart_none(
            self,
            get_active_cart_id_for_user_mock,
            get_cartdetails_from_id_mock,
            remove_product_from_cart_mock
    ):
        get_active_cart_id_for_user_mock.return_value = 1
        get_cartdetails_from_id_mock.return_value = [["1", "1", "1", 2]]
        user = users.User("username", "password", "name")
        remove_product_from_cart_mock.return_value = False
        self.assertFalse(cart_operations.remove_product_from_cart(user, "1"))

        get_active_cart_id_for_user_mock.return_value = None
        self.assertIsNone(cart_operations.remove_product_from_cart(user, "1"))

        get_cartdetails_from_id_mock.return_value = []
        self.assertIsNone(cart_operations.remove_product_from_cart(user, "1"))







