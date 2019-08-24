APP_NAME = "Desafio IMTS"
DEBUG = True 

DB_DRIVER = 'postgresql'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_DATABASE = 'postgres' # Redefinir
DB_USER = 'postgres' # Redefinir
DB_USER_PASSWORD = '85334206' # Redefinir

SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'\
    .format(DB_DRIVER, DB_USER, DB_USER_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True