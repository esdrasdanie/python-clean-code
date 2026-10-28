from flask import Blueprint, jsonify

users_bp = Blueprint('user_routes', __name__)


@users_bp.route('/user', methods=['POST'])
def registry_user():
    return jsonify({"rota": "Rota de cadastro estou dentro!"}), 200