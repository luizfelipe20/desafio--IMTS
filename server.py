import contact
from app.controllers import default
from flask import Flask


def create_app():
	app = Flask(__name__)
	default.configure(app)
	contact.configure(app)
	return app