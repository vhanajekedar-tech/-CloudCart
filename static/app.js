let cartCount = 0;

async function loadProducts() {
    const response = await fetch("/api/products");
    const products = await response.json();

    document.getElementById("products").innerHTML = products.map(product => `
        <div class="product">
            <h3>${product.name}</h3>
            <p class="price">₹${product.price}</p>
            <button onclick="addToCart()">Add to Cart</button>
        </div>
    `).join("");
}

function addToCart() {
    cartCount++;
    document.getElementById("cart-count").textContent = cartCount;
}

loadProducts();
