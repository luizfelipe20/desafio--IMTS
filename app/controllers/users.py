from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.tables import User
from app.serializers import UserSchema


bp_users = Blueprint('Users', __name__, url_prefix="/user")


@bp_users.route('/', methods=['get'])
@jwt_required
def list():
    result = User.query.all()
    return UserSchema(many=True).jsonify(result), 200


@bp_users.route('/<int:id>', methods=['delete'])
def delete(identificador):
    User.query.filter(User.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')


@bp_users.route('/<int:id>', methods=['update'])
def update(identificador):
    bs = UserSchema()
    query = User.query.filter(User.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())


@bp_users.route('/', methods=['post'])
def create():
    bs = UserSchema()
    user, error = bs.load(request.json)

    if error:
        return jsonify(error), 401

    current_app.db.session.add(user)
    current_app.db.session.commit()
    return bs.jsonify(user), 201



##################################
# @app.route("/users", methods=['GET'])
# def list():
# 	instance = User.query.all()
# 	return jsonify(data={})


# @app.route("/users/<int:id>", methods=['POST'])
# def create(id):
# 	if not(User.query.filter_by(id=id).first()):	
# 		instance = User("luiz_felipe", "85330", "Luiz Felipe", "felipekjs3@gmail.com")
# 		db.session.add(instance)
# 		db.session.commit()
# 	return "Criando!!!"


# @app.route("/users/<int:id>", methods=['UPDATE'])
# def update(id):
# 	if(User.query.filter_by(id=id).first()):
# 		instance = User.query.filter_by(username="luiz_felipe").first()
# 		instance.name = "Luiz F"
# 		db.session.add(instance)
# 		db.session.commit()
# 	return "Atualizando!!!"


# @app.route("/users/<int:id>", methods=['DELETE'])
# def delete(id):
# 	if(User.query.filter_by(id=id).first()):
# 		instance = User.query.filter_by(username="luiz_felipe").first()
# 		db.session.delete(instance)
# 		db.session.commit()
# 	return "Deletando!!!"
