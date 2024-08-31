from flask import Flask, request, jsonify

app = Flask(__name__)

# already some data is present of resource users 
users = {
    1: {'name': 'sai kiran', 'email': 'saikiranmandapati@gmail.com'},
    2: {'name': 'pwskills', 'email': 'pwskills@gmail.com'}
}

# to return all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# to get specific user by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# Creating a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not 'name' in data or not 'email' in data:
        return jsonify({'error': 'Bad request'}), 400

    new_id = max(users.keys()) + 1
    users[new_id] = {
        'name': data['name'],
        'email': data['email']
    }
    return jsonify(users[new_id]), 201

# Updating an existing user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']

    return jsonify(user)

# Deleting a user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
