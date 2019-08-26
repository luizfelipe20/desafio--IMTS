import uuid
import random

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql import UUID
from passlib.hash import pbkdf2_sha256


db = SQLAlchemy()


def configure(app):
	db.init_app(app)
	app.db = db

#  nome, username, password, telefone, aniversário e e-mail.
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String, nullable=False)
	name = db.Column(db.String)
	email = db.Column(db.String, unique=True)
	phone = db.Column(JSON)
	birthday = db.Column(db.DateTime, nullable=False)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	# def gen_hash(self):
	# 	self.password = pbkdf2_sha256.hash(self.password)

	# def verify_password(self, password):
	# 	return pbkdf2_sha256.verify(password, self.password)

	def __init__(self, username, password, name, email, phone, birthday):
		self.username = username 
		self.password = password
		self.name = name
		self.email = email
		self.phone = phone
		self.birthday = birthday

	def __repr__(self):
		return "{} {}".format(self.id, self.username)


# título, descrição, data início, data fim, data início inscrições, data fim inscrições
class Event(db.Model):	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	description = db.Column(db.Text)
	start_date = db.Column(db.DateTime, nullable=False)
	end_date = db.Column(db.DateTime, nullable=False)
	start_date_subscriptions = db.Column(db.DateTime, nullable=False)
	end_date_subscriptions = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User', foreign_keys=user_id)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __init__(self, title, description, start_date, end_date, start_date_subscriptions, end_date_subscriptions, user_id):
		self.title = title 
		self.description = description
		self.start_date = start_date
		self.end_date = end_date
		self.start_date_subscriptions = start_date_subscriptions
		self.end_date_subscriptions = end_date_subscriptions
		self.user_id = user_id

	def __repr__(self):
		return "{} {}".format(self.id, self.title)


class UserEvent(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User', foreign_keys=user_id)
	event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
	event = db.relationship('Event', foreign_keys=event_id)
	
	def __init__(self, user_id, event_id):
		self.user_id = user_id 
		self.event_id = event_id

	def __repr__(self):
		return "{}".format(self.id)	