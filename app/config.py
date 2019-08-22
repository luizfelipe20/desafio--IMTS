"""
Classe exemplo de Configurações Básicas do Servidor
"""
import os

class BaseConfig(object):
    APP_NAME = "Desafio IMTS"
    DEBUG = True 

    DB_DRIVER = os.getenv('DB_DRIVER', 'postgresql')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_DATABASE = os.getenv('DB_DATABASE', '') # Redefinir
    DB_USER = os.getenv('DB_USER', '') # Redefinir
    DB_USER_PASSWORD = os.getenv('DB_PASSWORD', '') # Redefinir
    
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'\
        .format(DB_DRIVER, DB_USER, DB_USER_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
