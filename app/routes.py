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

@bp.route('/categories')
def show_categories():
    sort_by = request.args.get('sort', 'id')
    direction = request.args.get('direction', 'asc')
    if direction not in ['asc', 'desc']:
        direction = 'asc'
    if sort_by == 'name':
        categories = Category.query.order_by(Category.name.asc() if direction == 'asc' else Category.name.desc()).all()
    else:
        categories = Category.query.order_by(Category.id.asc() if direction == 'asc' else Category.id.desc()).all()
    next_direction = 'desc' if direction == 'asc' else 'asc'
    return render_template('categories.html', categories=categories, sort=sort_by, direction=direction, next_direction=next_direction)

@bp.route('/brands')
def show_brands():
    sort_by = request.args.get('sort', 'id')
    direction = request.args.get('direction', 'asc')
    if direction not in ['asc', 'desc']:
        direction = 'asc'
    if sort_by == 'name':
        brands = Brand.query.order_by(Brand.name.asc() if direction == 'asc' else Brand.name.desc()).all()
    else:
        brands = Brand.query.order_by(Brand.id.asc() if direction == 'asc' else Brand.id.desc()).all()
    next_direction = 'desc' if direction == 'asc' else 'asc'
    return render_template('brands.html', brands=brands, sort=sort_by, direction=direction, next_direction=next_direction)