from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock in-memory data (auto-incrementing ID)
items = []
next_id = 1

# CREATE
@app.route('/items', methods=['POST'])
def create_item():
    global next_id
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    item = {
        'id': next_id,
        'name': data['name']
    }
    items.append(item)
    next_id += 1
    return jsonify(item), 201

# READ ALL
@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(items), 200

# READ ONE
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item['id'] == item_id:
            return jsonify(item), 200
    return jsonify({'error': 'Item not found'}), 404

# UPDATE
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()

    for item in items:
        if item['id'] == item_id:
            item['name'] = data.get('name', item['name'])
            return jsonify(item), 200

    return jsonify({'error': 'Item not found'}), 404

# DELETE
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

# Run app
if __name__ == '__main__':
    app.run(debug=True)
