from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

dbUser = 'root'
dbPassword = ''
dbHost = 'localhost'
dbName = 'storage'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + dbUser + ':' + dbPassword + '@' + dbHost + '/' + dbName
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    rating = db.Column(db.Numeric(3, 2), nullable=False)

@app.route('/products')
def show_products():
    sort = request.args.get('sort', 'id')
    direction = request.args.get('direction', 'asc')

    if sort not in ['id', 'name', 'category', 'brand', 'price', 'rating']:
        sort = 'id'
    if direction not in ['asc', 'desc']:
        direction = 'asc'

    # Toggle the direction for the next request
    next_direction = 'desc' if direction == 'asc' else 'asc'

    products = Product.query.order_by(getattr(getattr(Product, sort), direction)()).all()
    return render_template('products.html', products=products, sort=sort, direction=direction, next_direction=next_direction)


if __name__ == '__main__':
    app.run(debug=True)