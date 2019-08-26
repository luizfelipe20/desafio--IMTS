from app.models import tables as config_db
from app import serializers as config_ma
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from app import config_database
from app.controllers.users import bp_users
from app.controllers.login import bp_login
from app.controllers.events import bp_events


def create_app():
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


	app.register_blueprint(bp_users)
	app.register_blueprint(bp_login)
	app.register_blueprint(bp_events)
	return app