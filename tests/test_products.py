import unittest
from unittest.mock import patch
from src.classes import products
from src.operations import products_operations
from src.db_operations import products_db


class TestProducts(unittest.TestCase):

    def test_object_creation(self):
        product = products.Product("id", "name", "price", "4", tuple())
        self.assertIsInstance(product, products.Product)

    def test_object_creation_exceptions(self):
        self.assertRaises(ValueError, products.Product, "id", "name", "price", "invalid_quantity", (1, 2))

    @patch("src.db_operations.categories_db.get_category_names_for_all_product")
    @patch("src.operations.products_operations.show_all_products")
    def test_show_all_products(self,show_all_products_mock,get_category_names_for_all_product_mock):
        show_all_products_mock.return_value = []
        get_category_names_for_all_product_mock.return_value = []
        self.assertIsInstance(products_operations.show_all_products(), list)

    @patch("src.db_operations.categories_db.get_category_names_for_all_product")
    @patch("src.db_operations.products_db.get_all_products")
    def test_show_all_products(self,get_all_products_mock, get_category_names_for_all_product_mock):
        get_all_products_mock.return_value = [[1, "product_name", "1200", 3]]
        get_category_names_for_all_product_mock.return_value = [[1, "furniture"]]
        self.assertIsInstance(products_operations.show_all_products(), list)

    @patch("src.db_operations.products_db.get_all_products")
    def test_show_all_products_none(self, get_all_products_mock):
        get_all_products_mock.return_value = None
        self.assertIsNone(products_operations.show_all_products())

    @patch("src.db_operations.products_db.get_products_in_category")
    def test_get_products_by_category(self, get_products_in_category_mock):
        get_products_in_category_mock.return_value = [[1, "product_name", "1200", 3]]
        self.assertIsInstance(products_operations.get_products_by_category("furniture"), list)

    @patch("src.db_operations.products_db.get_products_in_category")
    def test_get_products_by_category_none(self, get_products_in_category_mock):
        get_products_in_category_mock.return_value = []
        self.assertIsNone(products_operations.get_products_by_category("furniture"))

    @patch("src.db_operations.products_db.get_products_details")
    def test_get_products_by_ids(self, get_product_details_mock):
        get_product_details_mock.return_value = [[1, "product_name", "1200", 3]]
        actual_result = products_operations.get_products_by_ids([1])
        self.assertIsInstance(actual_result,list)

    @patch("src.db_operations.products_db.get_products_details")
    def test_get_products_by_ids_none(self, get_product_details_mock):
        get_product_details_mock.return_value = []
        actual_result = products_operations.get_products_by_ids([1])
        self.assertIsNone(actual_result)

    @patch("src.db_operations.products_db.get_products_details")
    def test_get_product_details_if_can_be_added(self, get_product_details_mock):
        get_product_details_mock.return_value = [1, "product_name", "1200", 2]
        actual_result = products_operations.get_product_details_if_can_be_added(1,1)
        self.assertIsInstance(actual_result, products.Product)

    @patch("src.db_operations.products_db.get_product_details")
    def test_get_product_details_if_can_be_added_none(self, get_product_details_mock):
        get_product_details_mock.return_value = [1, "product_name", "1200", 2]
        actual_result = products_operations.get_product_details_if_can_be_added(1, 4)
        self.assertIsNone(actual_result)

        get_product_details_mock.return_value = [12, "product_name", "1200", 0]
        actual_result = products_operations.get_product_details_if_can_be_added(1, 3)
        self.assertIsNone(actual_result)



if __name__ == '__main__':
    unittest.main()
