from app.models.user import User
from app.extensions import db
from flask import jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta

def register_user(name, email, password):
    if not all([name, email, password]):
        return jsonify({"error": "All fields are required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 409

    user = User(name=name, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
        return {"message": "Login successful!", "token": access_token}, 200
    return {"error": "Invalid email or password"}, 401

import traceback

try:
    # login logic
except Exception as e:
    traceback.print_exc()
    return jsonify({'error': 'Internal server error'}), 500
