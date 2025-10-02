from flask import Flask,render_template ,jsonify,request

app=Flask(__name__)

@app.route("/")
def home():
    return "this is home page"


items=[
    {"id":1,"name":"sub1","description":"this is sub1"},
    {"id":2,"name":"sub2","description":"this is sub2"},
]

@app.route("/items",methods=["GET"])
def items_1():
    print(items)
    return jsonify(items)

@app.route("/items/<int:item_id>",methods=["GET"])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)


@app.route("/items",methods=["POST"])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json["name"],
        "description":request.json["description"]
    }
    
    items.append(new_item)
    return jsonify(new_item)

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Update only the fields provided
    item["name"] = data.get("name", item["name"])
    item["description"] = data.get("description", item["description"])

    return jsonify(item), 200


# ---------------- DELETE item ----------------
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "item not found"}), 404

    items = [i for i in items if i["id"] != item_id]
    return jsonify({"message": f"Item {item_id} deleted successfully"}), 200


if __name__=="__main__":
    app.run(debug=True)