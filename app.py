from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URL da sua aplicação Node.js
NODEJS_BASE_URL = "http://localhost:3000"

# Rotas para interagir com a aplicação Node.js
@app.route('/users', methods=['GET'])
def get_all_users():
    response = requests.get(f"{NODEJS_BASE_URL}/users")
    return jsonify(response.json())

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    response = requests.post(f"{NODEJS_BASE_URL}/users", json=user_data)
    return jsonify(response.json()), response.status_code

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user_data = request.get_json()
    response = requests.put(f"{NODEJS_BASE_URL}/users/{id}", json=user_data)
    return jsonify(response.json()), response.status_code

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    response = requests.delete(f"{NODEJS_BASE_URL}/users/{id}")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
