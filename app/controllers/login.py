from datetime import timedelta
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from app.models.tables import User
from app.serializers import UserSchema

bp_login = Blueprint('login', __name__)


@bp_login.route('/login', methods=['POST'])
def login():
    user = User(**request.json)

    if error:
        return jsonify(error), 401

    user = User.query.filter_by(username=user.username).first()

    if user and user.verify_password(request.json['password']):
        acess_token = create_access_token(
            identity=user.id,
        )
        refresh_token = create_refresh_token(identity=user.id)

        return jsonify({
            'acess_token': acess_token,
            'message': 'sucess'
        }), 200

    return jsonify({
        'message': 'As crendencias informadas não são válidas!'
    }), 401
