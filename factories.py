from faker import Faker

fake = Faker()

class ProductFactory:
    @staticmethod
    def create_fake_product():
        return {
            "name": fake.word(),
            "price": fake.random_number(digits=2),
            "description": fake.sentence(),
            "category": fake.word(),
            "quantity": fake.random_number(digits=2)
        }
