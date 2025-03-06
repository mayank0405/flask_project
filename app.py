from flask import Flask, request, jsonify

app = Flask(__name__)

reviews = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Movie Review API!"})

@app.route("/reviews", methods = ["POST"])
def add_review():
    data = request.json
    if not data or "title" not in data or "review" not in data:
        return jsonify({"message": "Invalid data"}), 400
    reviews.append(data)
    return jsonify({"message": "Review added successfully"}), 201

@app.route("/reviews", methods = ["GET"])
def get_reviews():
    return jsonify(reviews)

@app.route("/reviews/<int:index>", methods=["PUT"])
def update_review(index):
    if index < 0 or index >= len(reviews):
        return jsonify({"message": "Review not found"}), 404
    data = request.json
    if not data or "title" not in data or "review" not in data:
        return jsonify({"message": "Invalid Data"}), 400
    reviews[index] = data
    return jsonify({"message": "Review updated successfully"})

@app.route("/reviews/<int:index>", methods=["DELETE"])
def delete_review(index):
    if index < 0 or index >= len(reviews):
        return jsonify({"message": "Review not found"}), 404
    del reviews[index]
    return jsonify({"message": "Review deleted successfully"})


if __name__ == '__main__':
    app.run(debug = True)


    #To improve the code use dictionary
    '''
    ✅Faster Lookup, Update, and Deletion → O(1) average time complexity.
    ✅ No risk of index out-of-range errors like in lists.
    ✅ Easier to manage IDs rather than relying on list positions that may shift.
    '''
    #Link:  https://chatgpt.com/canvas/shared/67c94ac652188191a627864b36278c61
