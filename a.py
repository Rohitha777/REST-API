from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
users = []

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user['id'] == user_id:
            user['name'] = data.get('name', user['name'])
            user['email'] = data.get('email', user['email'])
            return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'}), 404

# Optional: homepage
@app.route('/')
def home():
    return "👋 Welcome! Go to /users to see the user list."

if __name__ == '__main__':
    app.run(debug=True)
