import unittest
from unittest.mock import patch
from src.classes import cartdetails, users, products
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
        user = users.User("username", "password", "name")
        remove_product_from_cart_mock.return_value = True

        self.assertTrue(cart_operations.remove_product_from_cart(user, "1"))

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

    @patch("src.db_operations.bill_db.create_new_bill")
    @patch("src.operations.bill_operations.get_id_and_quantity_if_products_can_be_billed_in_cart_of_user")
    @patch("src.operations.cart_operations.get_cart_data_to_print")
    @patch("src.db_operations.cart_db.get_active_cart_id_for_user")
    def test_checkout_cart(self,
                           get_active_cart_id_for_user_mock,
                           get_cart_data_to_print_mock,
                           get_id_and_quantity_if_products_can_be_billed_in_cart_of_user,
                           create_new_bill_mock
                           ):
        get_active_cart_id_for_user_mock.return_value = "1"
        get_cart_data_to_print_mock.return_value = ["non_empty_list", {"Total Amount": 1200, "Discount": 0}]
        get_id_and_quantity_if_products_can_be_billed_in_cart_of_user.return_value = ["ids_and_products"]
        create_new_bill_mock.return_value = ["new_bill"]
        user = users.User("username", "password", "name", 0)

        self.assertIsInstance(cart_operations.checkout_cart(user), list)

    @patch("src.db_operations.cart_db.get_active_cart_id_for_user")
    def test_checkout_cart_for_none_one(self,
                                        get_active_cart_id_for_user_mock
                                        ):
        get_active_cart_id_for_user_mock.return_value = None
        user = users.User("username", "password", "name", 0)
        self.assertIsNone(cart_operations.checkout_cart(user))

    @patch("src.operations.bill_operations.get_id_and_quantity_if_products_can_be_billed_in_cart_of_user")
    @patch("src.operations.cart_operations.get_cart_data_to_print")
    @patch("src.db_operations.cart_db.get_active_cart_id_for_user")
    def test_checkout_cart_for_none_two(self,
                                        get_active_cart_id_for_user_mock,
                                        get_cart_data_to_print_mock,
                                        get_id_and_quantity_if_products_can_be_billed_in_cart_of_user
                                        ):
        get_active_cart_id_for_user_mock.return_value = "1"
        get_cart_data_to_print_mock.return_value = ["non_empty_list", {"Total Amount": 1200, "Discount": 0}]
        get_id_and_quantity_if_products_can_be_billed_in_cart_of_user.return_value = []
        user = users.User("username", "password", "name", 0)

        self.assertIsNone(cart_operations.checkout_cart(user))

    @patch("src.db_operations.bill_db.create_new_bill")
    @patch("src.operations.bill_operations.get_id_and_quantity_if_products_can_be_billed_in_cart_of_user")
    @patch("src.operations.cart_operations.get_cart_data_to_print")
    @patch("src.db_operations.cart_db.get_active_cart_id_for_user")
    def test_checkout_cart(self,
                           get_active_cart_id_for_user_mock,
                           get_cart_data_to_print_mock,
                           get_id_and_quantity_if_products_can_be_billed_in_cart_of_user,
                           create_new_bill_mock
                           ):
        get_active_cart_id_for_user_mock.return_value = "1"
        get_cart_data_to_print_mock.return_value = ["non_empty_list", {"Total Amount": 1200, "Discount": 0}]
        get_id_and_quantity_if_products_can_be_billed_in_cart_of_user.return_value = ["ids_and_products"]
        create_new_bill_mock.return_value = []
        user = users.User("username", "password", "name", 0)

        self.assertIsNone(cart_operations.checkout_cart(user))

    @patch("src.operations.cart_operations.get_cart_and_product_details")
    def test_get_cart_data_to_print(self, get_cart_and_product_details_mock):
        get_cart_and_product_details_mock.return_value = [cartdetails.CartDetails("1", "1", "1", 2)],[products.Product("1","chair",1200, 5)]
        self.assertIsInstance(cart_operations.get_cart_data_to_print("username"), list)
