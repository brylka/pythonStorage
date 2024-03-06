from flask import Blueprint, render_template, request
from app.models import Product, Category, Brand

bp = Blueprint('main', __name__)

@bp.route('/products')
def show_products():
    sort = request.args.get('sort', 'id')
    direction = request.args.get('direction', 'asc')
    if direction not in ['asc', 'desc']:
        direction = 'asc'

    base_query = Product.query

    if sort in ['category', 'brand']:
        if sort == 'category':
            base_query = base_query.join(Category).order_by(getattr(Category.name, direction)())
        elif sort == 'brand':
            base_query = base_query.join(Brand).order_by(getattr(Brand.name, direction)())
    else:
        if sort not in ['id', 'name', 'price', 'rating']:
            sort = 'id'
        base_query = base_query.order_by(getattr(getattr(Product, sort), direction)())

    products = base_query.all()

    next_direction = 'desc' if direction == 'asc' else 'asc'

    return render_template('products.html', products=products, sort=sort, direction=direction, next_direction=next_direction)