from faker import Faker
import random

from app import create_app, db
from app.models import Product, Category, Brand

app = create_app()
app.app_context().push()

fake = Faker()


def add_categories_and_brands(number=5):
    for _ in range(number):
        category_name = fake.word().capitalize()
        if not Category.query.filter_by(name=category_name).first():
            category = Category(name=category_name)
            db.session.add(category)

        brand_name = fake.company()
        if not Brand.query.filter_by(name=brand_name).first():
            brand = Brand(name=brand_name)
            db.session.add(brand)
    db.session.commit()


def add_random_products(number=10):
    categories = Category.query.all()
    brands = Brand.query.all()

    for _ in range(number):
        name = fake.word().capitalize()
        category = random.choice(categories)
        brand = random.choice(brands)
        price = round(random.uniform(5.0, 100.0), 2)  # Generuje losowe ceny w zakresie od 5 do 100
        rating = round(random.uniform(1.0, 5.0), 2)  # Generuje losowe oceny w zakresie od 1 do 5

        product = Product(name=name, category_id=category.id, brand_id=brand.id, price=price, rating=rating)
        db.session.add(product)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        add_categories_and_brands(5)
        add_random_products(20)