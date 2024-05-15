from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# layanan produk
def get_product(product_id):
    response = requests.get(f'http://localhost:5000/products/{product_id}')
    return response.json()

# layanan get quantity dari keranjang
def get_sold_quantity(product_id):
    response = requests.get(f'http://localhost:5001/cart/quantity/{product_id}')
    return response.json()['total_quantity']

# layanan review
def get_reviews(product_id):
    response = requests.get(f'http://localhost:5003/reviews/{product_id}')
    return response.json()

@app.route('/product/<int:product_id>')
def get_product_info(product_id):
    # get layanan product
    product_info = get_product(product_id)
    # get layanan cart
    sold_products = get_sold_quantity(product_id)
    # get layanan revies
    product_reviews = get_reviews(product_id)

    return render_template('index.html', info=product_info, sold=sold_products, reviews=product_reviews)

if __name__ == '__main__':
    app.run(debug=True, port=5004)