from flask import jsonify
from app import app, db

@app.route("/users", methods=['GET'])
def list():
	instance = User.query.all()
	return jsonify(data={})


@app.route("/users/<int:id>", methods=['POST'])
def create(id):
	if not(User.query.filter_by(id=id).first()):	
		instance = User("luiz_felipe", "85330", "Luiz Felipe", "felipekjs3@gmail.com")
		db.session.add(instance)
		db.session.commit()
	return "Criando!!!"


@app.route("/users/<int:id>", methods=['UPDATE'])
def update(id):
	if(User.query.filter_by(id=id).first()):
		instance = User.query.filter_by(username="luiz_felipe").first()
		instance.name = "Luiz F"
		db.session.add(instance)
		db.session.commit()
	return "Atualizando!!!"


@app.route("/users/<int:id>", methods=['DELETE'])
def delete(id):
	if(User.query.filter_by(id=id).first()):
		instance = User.query.filter_by(username="luiz_felipe").first()
		db.session.delete(instance)
		db.session.commit()
	return "Deletando!!!"
