import contact
# import db
import admin

from app.models import tables as config_db
from app import serializers as config_ma
from app.controllers import default
from app.controllers.users import bp_users
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from app import config_database

def create_app():
	# app = Flask(__name__, template_folder='/foo/bancoar', static_folder='/foo/bar')
	# criacao do app
	app = Flask(__name__)

	#confguracoes do banco postgre
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config_database.SQLALCHEMY_TRACK_MODIFICATIONS
	app.config["SQLALCHEMY_DATABASE_URI"] = config_database.SQLALCHEMY_DATABASE_URI 
	app.config['JWT_SECRET_KEY'] = 'teste imst crl dev'

	

	config_db.configure(app)
	config_ma.configure(app)

	Migrate(app, app.db)


	CORS(app)

    
	JWTManager(app)


	#conexao com o banco nosql
	# db.configure(app)

	
	#view default para teste
	default.configure(app)
	

	# flask admin
	# admin.configure(app)


	#formulario de contato
	contact.configure(app)


	app.register_blueprint(bp_users)
	return app