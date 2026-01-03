#!/usr/bin/python3
"""Task 4: Flask REST API with user management."""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Welcome endpoint."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Get all usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """API status check."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Get user by username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add new user."""
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400
    
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
