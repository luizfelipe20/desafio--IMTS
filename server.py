import contact
import db
import admin
from app.controllers import default
from flask import Flask


def create_app():
	# app = Flask(__name__, template_folder='/foo/bar', static_folder='/foo/bar')
	# criacao do app
	app = Flask(__name__)

	
	#conexao com o banco
	db.configure(app)

	
	#view default para teste
	default.configure(app)
	

	# flask admin
	admin.configure(app)

	#formulario de contato
	contact.configure(app)
	return app