import contact
import admin
from app.controllers import default
from flask import Flask


def create_app():
	# app = Flask(__name__, template_folder='/foo/bar', static_folder='/foo/bar')
	app = Flask(__name__)
	default.configure(app)
	admin.configure(app)
	contact.configure(app)
	return app