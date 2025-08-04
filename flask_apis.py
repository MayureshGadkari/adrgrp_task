from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
data_store = []

# GET endpoint: fetch all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store), 200

# POST endpoint: add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    
    if not new_item or 'name' not in new_item:
        return jsonify({'error': 'Invalid input'}), 400

    data_store.append(new_item)
    return jsonify({'message': 'Item added', 'item': new_item}), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
