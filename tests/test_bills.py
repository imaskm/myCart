from unittest import TestCase
from unittest.mock import patch
from src.classes import bills
from src.operations import bill_operations
from src.db_operations import bill_db


class TestBills(TestCase):
    def test_object_creation(self):
        bill = bills.Bill(10000, 0, "1", "username")
        self.assertIsInstance(bill, bills.Bill)

    @patch("src.db_operations.bill_db.get_bill_data_for_user")
    def test_get_bill_for_user(self, get_bill_data_for_user_mock):
        get_bill_data_for_user_mock.return_value = [["1", 10000, 0, "1", "username"]]

        self.assertIsInstance(bill_operations.get_bill_for_user("username"), list)

    @patch("src.db_operations.bill_db.get_bill_data_for_user")
    def test_get_bill_for_user_for_none(self, get_bill_data_for_user_mock):
        get_bill_data_for_user_mock.return_value = []
        self.assertIsNone(bill_operations.get_bill_for_user("username"))
