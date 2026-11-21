from flask import Flask, jsonify, render_template
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

products = [
    {"id": 1, "name": "Wireless Headphones", "price": 1499},
    {"id": 2, "name": "Smart Watch", "price": 1999},
    {"id": 3, "name": "Bluetooth Speaker", "price": 999},
    {"id": 4, "name": "Laptop Backpack", "price": 799}
]

REQUEST_COUNT = Counter(
    'cloudcart_requests_total',
    'Total number of CloudCart requests',
    ['endpoint']
)

@app.before_request
def count_requests():
    from flask import request
    REQUEST_COUNT.labels(endpoint=request.endpoint or 'unknown').inc()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/products")
def get_products():
    return jsonify(products)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
