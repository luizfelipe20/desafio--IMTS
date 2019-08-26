from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.tables import User
from app.serializers import UserSchema


bp_users = Blueprint('user', __name__, url_prefix="/user")


@bp_users.route('/', methods=['get'])
# @jwt_required
def list():
    result = User.query.all()
    return UserSchema(many=True).jsonify(result), 200


@bp_users.route('/<int:id>', methods=['delete'])
def delete(id):
    user_exists = User.query.filter(User.id == id).first()
    if user_exists: 
        User.query.filter(User.id == id).delete()
        current_app.db.session.commit()
        return jsonify('Deletado!!!!')
    else:
        return jsonify({
            'message': 'Registro não encontrado!.'
        }), 400


@bp_users.route('/<int:id>', methods=['patch'])
def update(id):
    user_exists = User.query.filter(User.id == id).first()
    if user_exists:
        user_schema = UserSchema()
        query = User.query.filter(User.id == id)
        query.update(request.json)
        current_app.db.session.commit()
        return user_schema.jsonify(query.first())
    else:
        return jsonify({
            'message': 'Registro não encontrado!.'
        }), 400

@bp_users.route('/', methods=['post'])
def create():
    user_schema = UserSchema()
    username = request.json["username"]
    password = request.json["password"]
    
    user_exists = User.query.filter_by(username=username).first()
    
    # import ipdb; ipdb.set_trace()
    # print("user_exists", user_exists)

    if not user_exists:
        new_user = User(username, password)
    else:
        return jsonify({
            'message': 'Este usuário já foi registrado!.'
        }), 400

    current_app.db.session.add(new_user)
    current_app.db.session.commit()

    return user_schema.jsonify(new_user), 201
