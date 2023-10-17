from flask import Flask, request, jsonify

app = Flask(__name__)

# Create a list to act as a simple database.
database = ['ab-list','ab-list2']

# Route for creating a new item.
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    database.append(data)
    return jsonify(data), 201

# Route for retrieving all items.
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(database)

# Route for updating an item by index.
@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    data = request.json
    if 0 <= index < len(database):
        database[index] = data
        return jsonify(data)
    return "Item not found", 404

# Route for deleting an item by index.
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if 0 <= index < len(database):
        deleted_item = database.pop(index)
        return jsonify(deleted_item)
    return "Item not found", 404

if __name__ == '__main__':
    app.run(debug=True)
