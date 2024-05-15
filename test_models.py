import unittest
from service.models import Product, Category
from service.database import Database

class TestProductModel(unittest.TestCase):

    def setUp(self):
        # Set up test data or initialize database connection
        self.db = Database()
        self.product1 = Product(name="Test Product 1", price=10.0, category=Category.CLOTHS, available=True)
        self.product2 = Product(name="Test Product 2", price=20.0, category=Category.TOOLS, available=False)
        self.db.add_product(self.product1)
        self.db.add_product(self.product2)

    def tearDown(self):
        # Clean up test data or close database connection
        self.db.delete_product(self.product1)
        self.db.delete_product(self.product2)

    def test_read_product(self):
        # Test the read product function
        product = self.db.get_product(self.product1.id)
        self.assertEqual(product.name, "Test Product 1")

    def test_update_product(self):
        # Test the update product function
        updated_product = Product(id=self.product1.id, name="Updated Product", price=15.0, category=Category.FOOD, available=False)
        self.db.update_product(updated_product)
        product = self.db.get_product(self.product1.id)
        self.assertEqual(product.name, "Updated Product")

    def test_delete_product(self):
        # Test the delete product function
        self.db.delete_product(self.product1)
        product = self.db.get_product(self.product1.id)
        self.assertIsNone(product)

    def test_list_all_products(self):
        # Test the list all products function
        products = self.db.get_all_products()
        self.assertEqual(len(products), 2)

    def test_find_by_name(self):
        # Test the find by name function
        products = self.db.find_products_by_name("Test Product 1")
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, "Test Product 1")

    def test_find_by_category(self):
        # Test the find by category function
        products = self.db.find_products_by_category(Category.TOOLS)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].category, Category.TOOLS)

    def test_find_by_availability(self):
        # Test the find by availability function
        products = self.db.find_products_by_availability(True)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].available, True)

if __name__ == '__main__':
    unittest.main()
