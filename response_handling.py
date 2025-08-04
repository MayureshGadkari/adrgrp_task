from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store
items = []

# POST endpoint: Receive JSON and store item
@app.route('/items', methods=['POST'])
def create_item():
    try:
        data = request.get_json()  # Get JSON data from request
        name = data.get('name')
        quantity = data.get('quantity')

        if not name or not isinstance(quantity, int):
            return jsonify({'error': 'Invalid input'}), 400

        item = {'name': name, 'quantity': quantity}
        items.append(item)

        return jsonify({'message': 'Item created', 'item': item}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# GET endpoint: Return all items as JSON
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': items}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
