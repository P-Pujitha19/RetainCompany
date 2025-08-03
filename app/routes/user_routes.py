from flask import Blueprint, request, jsonify
from app.services.user_service import register_user, login_user
from app.models.user import User
from app.extensions import db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    return register_user(name, email, password)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    return login_user(email, password)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.serialize()), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200

@user_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name', '')
    users = User.query.filter(User.name.ilike(f"%{name}%")).all()
    return jsonify([user.serialize() for user in users]), 200

@user_bp.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200
