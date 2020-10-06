import unittest
from unittest.mock import patch
from src.classes import categories
from src.operations import category_operations

class TestCategories(unittest.TestCase):

    def test_object_creation(self):
        self.assertIsInstance(categories.Category("id", "name"), categories.Category)

    @patch("src.db_operations.categories_db.get_all_categories")
    def test_show_all_category(self, get_all_categories_mock):
        get_all_categories_mock.return_value = [[1, "furniture"]]
        self.assertIsInstance(category_operations.show_all_categories(),list)

    @patch("src.db_operations.categories_db.get_all_categories")
    def test_show_all_category_none(self, get_all_categories_mock):
        get_all_categories_mock.return_value = []
        self.assertIsNone(category_operations.show_all_categories())


if __name__ == '__main__':
    unittest.main()
