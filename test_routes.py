def test_update_product(self):
    # Test the update product function
    updated_product = Product(id=self.product1.id, name="Updated Product", price=15.0, category=Category.FOOD, available=False)
    self.db.update_product(updated_product)
    product = self.db.get_product(self.product1.id)
    self.assertEqual(product.name, "Updated Product")
