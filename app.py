from flask import Flask, render_template, redirect, url_for, jsonify

app = Flask(__name__)

# ==========================================
# PRODUCTS
# ==========================================

products = [
    {
        "id": 1,
        "name": "Lipstick",
        "brand": "Maybelline",
        "price": 399,
        "image": "lipstick1.jpg",
    },
    {
        "id": 2,
        "name": "Lip Balm",
        "brand": "Nivea",
        "price": 199,
        "image": "lipbalm1.jpg",
    },
    {
        "id": 3,
        "name": "Foundation",
        "brand": "Lakme",
        "price": 599,
        "image": "foundation1.jpg",
    },
    {
        "id": 4,
        "name": "Compact Powder",
        "brand": "Faces Canada",
        "price": 349,
        "image": "model1.jpg",
    },
    {
        "id": 5,
        "name": "Eyeliner",
        "brand": "Lakme",
        "price": 250,
        "image": "eyeliner1.jpg",
    },
    {
        "id": 6,
        "name": "Mascara",
        "brand": "Maybelline",
        "price": 499,
        "image": "mascara1.jpg",
    },
    {
        "id": 7,
        "name": "Nail Polish",
        "brand": "Colorbar",
        "price": 180,
        "image": "nailpolish1.jpg",
    },
    {
        "id": 8,
        "name": "Perfume",
        "brand": "Bella Vita",
        "price": 799,
        "image": "perfume1.jpg",
    },
    {
        "id": 9,
        "name": "Face Wash",
        "brand": "Himalaya",
        "price": 220,
        "image": "facewash1.jpg",
    },
    {
        "id": 10,
        "name": "Moisturizer",
        "brand": "Pond's",
        "price": 299,
        "image": "moisturizer1.jpg",
    },
    {
        "id": 11,
        "name": "Sunscreen",
        "brand": "Aqualogica",
        "price": 499,
        "image": "sunscreen1.jpg",
    },
    {
        "id": 12,
        "name": "Blush",
        "brand": "Swiss Beauty",
        "price": 349,
        "image": "blush1.jpg",
    },
    {
        "id": 13,
        "name": "Concealer",
        "brand": "Insight",
        "price": 275,
        "image": "concealer1.jpg",
    },
    {
        "id": 14,
        "name": "Eyeshadow Palette",
        "brand": "Mars",
        "price": 699,
        "image": "eyeshadow1.jpg",
    },
    {
        "id": 15,
        "name": "Makeup Remover",
        "brand": "Garnier",
        "price": 249,
        "image": "remover1.jpg",
    },
]

# ==========================================
# CART
# ==========================================

cart = []

# ==========================================
# HOME PAGE
# ==========================================


@app.route("/")
def home():

    total = sum(item["price"] for item in cart)

    return render_template("index.html", products=products, cart=cart, total=total)


# ==========================================
# ADD TO CART
# ==========================================


@app.route("/add/<int:id>")
def add(id):

    for product in products:

        if product["id"] == id:

            cart.append(product)

            break

    total = sum(item["price"] for item in cart)

    return jsonify(
        {"success": True, "cart_count": len(cart), "total": total, "cart": cart}
    )


# ==========================================
# REMOVE FROM CART
# ==========================================


@app.route("/remove/<int:id>")
def remove(id):

    for item in cart:

        if item["id"] == id:

            cart.remove(item)

            break

    total = sum(item["price"] for item in cart)

    return jsonify(
        {"success": True, "cart_count": len(cart), "total": total, "cart": cart}
    )


# ==========================================
# CLEAR CART
# ==========================================


@app.route("/clear")
def clear():

    cart.clear()

    return redirect(url_for("home"))


# ==========================================
# CHECKOUT
# ==========================================


@app.route("/checkout")
def checkout():

    total = sum(item["price"] for item in cart)

    return render_template("checkout.html", cart=cart, total=total)


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
