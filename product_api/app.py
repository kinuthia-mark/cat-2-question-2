from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (dictionary for simplicity)
products = []
product_id_counter = 1

# Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    global product_id_counter
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    # Add new product
    product = {
        'id': product_id_counter,
        'name': data['name'],
        'description': data['description'],
        'price': float(data['price']),
    }
    products.append(product)
    product_id_counter += 1
    return jsonify(product), 201

# Retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
