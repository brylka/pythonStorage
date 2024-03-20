from flask import Blueprint, render_template, request, redirect, url_for
from app import db
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

@bp.route('/categories/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            new_category = Category(name=name)
            db.session.add(new_category)
            db.session.commit()
            return redirect(url_for('main.show_categories'))
    return render_template('category_add.html')

@bp.route('/categories/edit/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        return redirect(url_for('main.show_categories'))
    return render_template('category_edit.html', category=category)

@bp.route('/categories/delete/<int:id>', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('main.show_categories'))

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

@bp.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        category_id = request.form.get('category_id')
        brand_id = request.form.get('brand_id')
        price = request.form.get('price')
        rating = request.form.get('rating')
        if name:
            new_product = Product(name=name, category_id=category_id, brand_id=brand_id, price=price, rating=rating)
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('main.show_products'))
    return render_template('product_add.html')