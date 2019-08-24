from tinymongo import TinyMongoClient


def get_db():
	conn = TinyMongoClient()
	#cria um arquivo para registrar com este nome
	db = conn.my_database
	return db


def configure(app):
	app.db = get_db()