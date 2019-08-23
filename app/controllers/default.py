from flask import render_template
from app import app, db
from app.models.tables import User
from app.models.forms import LoginForm


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


@app.route("/insert_db", methods=['GET'])
def insert_db():
	instance = User("luiz_felipe", "85330", "Luiz Felipe", "felipekjs3@gmail.com")
	db.session.add(instance)
	db.session.commit()
	return "OK"


# @app.route("/login", methods=['GET', 'POST'])
# def login():
# 	form = loginForm()
# 	if form.validate_on_submit():
# 		print("user", form.username.data)
# 	return render_template('login.html', form=form)
