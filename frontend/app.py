from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)
app.secret_key = "frontend-secret-key"

# Enable simple CORS support
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# URL provider services
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:5001")
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://localhost:5002")
ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL", "http://localhost:5003")

# Routes
@app.route('/')
def index():
    return render_template('index.html')

# User routes
@app.route('/users')
def users_page():
    return render_template('users.html')

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        # Simulate endpoint to get all users
        users = []
        # Try to get users with IDs 1-20
        for user_id in range(1, 21):
            try:
                response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}", timeout=0.5)
                if response.status_code == 200:
                    users.append(response.json())
            except:
                continue
        return jsonify(users), 200
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to User Service"}), 503

@app.route('/api/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        response = requests.post(f"{USER_SERVICE_URL}/users", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to User Service"}), 503

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to User Service"}), 503

# Product routes
@app.route('/products')
def products_page():
    return render_template('products.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        # Simulate endpoint to get all products
        products = []
        # Try to get products with IDs 1-20
        for product_id in range(1, 21):
            try:
                response = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}", timeout=0.5)
                if response.status_code == 200:
                    products.append(response.json())
            except:
                continue
        return jsonify(products), 200
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to Product Service"}), 503

@app.route('/api/products', methods=['POST'])
def create_product():
    try:
        data = request.json
        response = requests.post(f"{PRODUCT_SERVICE_URL}/products", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to Product Service"}), 503

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        response = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to Product Service"}), 503

# Order routes
@app.route('/orders')
def orders_page():
    return render_template('orders.html')

@app.route('/api/orders', methods=['GET'])
def get_orders():
    try:
        # Simulate endpoint to get all orders
        orders = []
        # Try to get orders with IDs 1-20
        for order_id in range(1, 21):
            try:
                response = requests.get(f"{ORDER_SERVICE_URL}/orders/{order_id}", timeout=0.5)
                if response.status_code == 200:
                    orders.append(response.json())
            except:
                continue
        return jsonify(orders), 200
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to Order Service"}), 503

@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        data = request.json
        response = requests.post(f"{ORDER_SERVICE_URL}/orders", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to Order Service"}), 503

@app.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        response = requests.get(f"{ORDER_SERVICE_URL}/orders/{order_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to Order Service"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
