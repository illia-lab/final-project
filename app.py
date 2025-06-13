from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

products = [
    {'id': 1, 'name': 'Ефіопська Арабіка', 'price': 240, 'image': '/image/coffee1.jpeg'},
    {'id': 2, 'name': 'Бразильська кава з горіхами', 'price': 195, 'image': '/image/coffee2.jpg'},
     {'id': 3, 'name': 'Екзцелса', 'price': 325, 'image': '/image/coffee1.jpeg'},
    {'id': 4, 'name': 'Робуста', 'price': 410, 'image': '/image/coffee2.jpg'},
     {'id': 5, 'name': 'Ліберіка', 'price': 130, 'image': '/image/coffee1.jpeg'},
    {'id': 6, 'name': 'Стенофіла', 'price': 190, 'image': '/image/coffee2.jpg'},
     {'id': 7, 'name': 'Бразильська Сантос', 'price': 260, 'image': '/image/coffee1.jpeg'},
    {'id': 8, 'name': 'Колумбійська Супремо', 'price': 1000, 'image': '/image/coffee2.jpg'},
         {'id': 9, 'name': 'Суматра Менделінг', 'price': 750, 'image': '/image/coffee1.jpeg'},
    {'id': 10, 'name': 'Кенійська АА', 'price': 3200, 'image': '/image/coffee2.jpg'},
]

@app.route('/products')
def product_page():
    return render_template('products.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('product_page'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart=cart_items)

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]
    session['cart'] = cart
    return redirect(url_for('cart'))

if __name__ == ("__main__"):
    app.run(debug = True)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart=cart_items, total=total)


