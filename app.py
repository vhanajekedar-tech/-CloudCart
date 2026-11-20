from flask import Flask, jsonify, render_template

app = Flask(__name__)

products = [
    {"id": 1, "name": "Wireless Headphones", "price": 1499},
    {"id": 2, "name": "Smart Watch", "price": 1999},
    {"id": 3, "name": "Bluetooth Speaker", "price": 999},
    {"id": 4, "name": "Laptop Backpack", "price": 799}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/products")
def get_products():
    return jsonify(products)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
