from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from app.config import BaseConfig

"""
Instanciando Banco/SQLAlchemy e suas Migrações:
"""
migrate = Migrate()
db = SQLAlchemy()

def create_app(*args, **kwargs):
    flask_app = Flask(__name__)

    # Inicializando o Servidor com o arquivo de configuração:
    #flask_app.config.from_object(BaseConfig)

    #CORS(flask_app)

    #db.init_app(flask_app)
    #migrate.init_app(flask_app, db)
   
    return flask_app