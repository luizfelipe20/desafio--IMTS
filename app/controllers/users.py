from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.tables import User
from app.serializers import UserSchema


bp_users = Blueprint('user', __name__, url_prefix="/user")


@bp_users.route('/', methods=['get'])
@jwt_required
def list():
    result = User.query.all()
    return UserSchema(many=True).jsonify(result), 200


@bp_users.route('/<int:id>', methods=['delete'])
def delete(id):
    User.query.filter(User.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')


@bp_users.route('/<int:id>', methods=['update'])
def update(id):
    bs = UserSchema()
    query = User.query.filter(User.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())


@bp_users.route('/', methods=['post'])
def create():
    us = UserSchema()

    user, error = us.load(request.json)

    if error:
        return jsonify(error), 401

    user.gen_hash()

    current_app.db.session.add(user)
    current_app.db.session.commit()

    return us.jsonify(user), 201
