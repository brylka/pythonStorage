from app import db, app
from app import Product
from faker import Faker
import random

def add_random_products(number=10):
    fake = Faker()
    for _ in range(number):
        name = fake.word().capitalize()
        category = fake.word().capitalize()
        brand = fake.company()
        price = round(random.uniform(5.0, 100.0), 2)  # Generuje losowe ceny w zakresie od 5 do 100
        rating = round(random.uniform(1.0, 5.0), 2)  # Generuje losowe oceny w zakresie od 1 do 5

        product = Product(name=name, category=category, brand=brand, price=price, rating=rating)
        db.session.add(product)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        add_random_products(10)