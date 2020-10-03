import unittest
from src.classes import products


class TestProducts(unittest.TestCase):

    def test_object_creation(self):
        product = products.Product("id", "name", "price", "4", tuple())
        self.assertIsInstance(product, products.Product)


if __name__ == '__main__':
    unittest.main()
