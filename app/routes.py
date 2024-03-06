from flask import Blueprint, render_template, request
from app.models import Product

bp = Blueprint('main', __name__)

@bp.route('/products')
def show_products():
    sort = request.args.get('sort', 'id')
    direction = request.args.get('direction', 'asc')
    if sort not in ['id', 'name', 'category', 'brand', 'price', 'rating']:
        sort = 'id'
    if direction not in ['asc', 'desc']:
        direction = 'asc'
    next_direction = 'desc' if direction == 'asc' else 'asc'
    products = Product.query.order_by(getattr(getattr(Product, sort), direction)()).all()
    return render_template('products.html', products=products, sort=sort, direction=direction, next_direction=next_direction)
