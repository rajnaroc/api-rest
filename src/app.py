from flask import Flask, jsonify, request
from products import products
from flask_cors import CORS
from flask import send_from_directory
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": 'http://127.0.0.1:5500'}})

@app.before_request
def before_request():
    print("Antes de la petición")

@app.after_request
def after_request(response):
    print("Despues de la petición")
    return response

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message": "List of products"})

@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not found"})

@app.route('/products', methods=['POST'])
def add_product():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity'],
        "description": request.json.get('description', '')
    }
    products.append(new_product)
    return jsonify({"message": "Product added successfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def edit_product(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound) != 0:
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        productFound[0]['description'] = request.json.get('description', '')
        return jsonify({
            "message": "Product updated",
            "product": productFound[0]
        })

@app.route('/query_string', methods=['GET'])
def query_string():
    print(request)
    print(request.query_string)
    print(request.args)
    print(request.args.get('page'))
    print(request.args.get('jhon'))
    print(request.args.get('pepe'))
    return "Ok"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)