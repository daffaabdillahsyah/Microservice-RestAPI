from flask import Flask, jsonify

app = Flask(__name__)

product_reviews =[
    {"user_id": 1, "product_id": 1, "review": "very good"},
    {"user_id": 2, "product_id": 3, "review": "good"},
    {"user_id": 3, "product_id": 2, "review": "not good"},
    {"user_id": 4, "product_id": 1, "review": "ew"},
    {"user_id": 5, "product_id": 2, "review": "well"},
    {"user_id": 6, "product_id": 2, "review": "nice"},
    {"user_id": 7, "product_id": 3, "review": "not bad"},
    {"user_id": 8, "product_id": 1, "review": "love it"},
    {"user_id": 9, "product_id": 1, "review": "well done"},
    {"user_id": 10, "product_id": 2, "review": "cool"},
    {"user_id": 11, "product_id": 3, "review": "nice fruit"},
    {"user_id": 12, "product_id": 3, "review": "yummy"},
    {"user_id": 13, "product_id": 3, "review": "nomnom"},
    {"user_id": 14, "product_id": 2, "review": "no"},
    {"user_id": 15, "product_id": 2, "review": "yes"},
    
]

@app.route("/reviews")
def get_reviews():
    return jsonify(product_reviews)

# get reviews by product
@app.route("/reviews/<int:product_id>")
def get_review(product_id):
    reviews = [review for review in product_reviews if review['product_id'] == product_id]
    if reviews:
        return jsonify(
            {"product_id": product_id},
            {"reviews": reviews},
        )
    else:
        return jsonify(
            {"message": "Product not found"},
            404
        )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)