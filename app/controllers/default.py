from flask import render_template, flash
from flask_login import login_user
from app import app, db, lm
from app.models.tables import User
from app.models.forms import LoginForm


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    return "Hello World! <strong>I am learning Flask</strong>", 200


# @app.route("/test", defaults={'name': None})
# @app.route("/test/<name>")
# def test(name):
# 	if name:
# 		return "Olá, {}".format(name)
# 	else:
# 		return "Olá, usuário!"


# @app.route("/test/<int:id>", methods=['GET'])
# def test(id):
# 	return "Olá, {}".format(id)


@app.route("/insert", methods=['GET'])
def insert():
	instance = User("luiz_felipe", "85330", "Luiz Felipe", "felipekjs3@gmail.com")
	db.session.add(instance)
	db.session.commit()
	return "OK"


@app.route("/list", methods=['GET'])
def list():
	instance = User.query.filter_by(username="luiz_felipe").all()
	print("instance", instance)	
	return "OK"


@app.route("/update", methods=['GET'])
def update():
	instance = User.query.filter_by(username="luiz_felipe").first()
	instance.name = "Luiz F"
	db.session.add(instance)
	db.session.commit()
	print("instance", instance)	
	return "OK"


@app.route("/delete", methods=['GET'])
def delete():
	instance = User.query.filter_by(username="luiz_felipe").first()
	db.session.delete(instance)
	db.session.commit()
	print("instance", instance)	
	return "OK"


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = loginForm()
	if form.validate_on_submit():
		user = User.User.query.filter_by(username="luiz_felipe").first()
		if user  and user.password == form.password.data:
			login_user(user)
			flash("Logged in.")
			return redirect(url_for("index"))
		else:
			flash("Invalid login.")	
	else:
		print(form.erros)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
	flash("Logged out.")
	return redirect(url_for("index"))



