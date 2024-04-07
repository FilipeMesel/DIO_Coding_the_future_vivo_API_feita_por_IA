from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados de exemplo para simular um banco de dados
users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    users.append(data)
    return jsonify({'message': 'User created successfully'})

@app.route('/users/<cpf>', methods=['GET'])
def get_user(cpf):
    for user in users:
        if user['cpf'] == cpf:
            return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<cpf>', methods=['PUT'])
def update_user(cpf):
    data = request.get_json()
    for user in users:
        if user['cpf'] == cpf:
            user.update(data)
            return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<cpf>', methods=['DELETE'])
def delete_user(cpf):
    global users
    users = [user for user in users if user['cpf'] != cpf]
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
