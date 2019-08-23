import uuid

from app import db
from datetime import datetime 
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql import UUID


#  nome, username, password, telefone, aniversário e e-mail.
class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.String(), nullable=False, default=uuid.uuid4().hex, primary_key=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	name = db.Column(db.String)
	email = db.Column(db.String, unique=True)
	phone = db.Column(JSON)
	birthday = db.Column(db.DateTime, nullable=False)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __init__(self, username, password, name, email, phone, birthday):
		self.username = username
		self.password = password
		self.name = name
		self.email = email
		self.phone = phone
		self.birthday = birthday

	def __repr__(self):
		return "{}".format(self.id, self.username)


# título, descrição, data início, data fim, data início inscrições, data fim inscrições
class Event(db.Model):
	__tablename__ = "events"		


	id = db.Column(db.String(), nullable=False, default=uuid.uuid4().hex, primary_key=True)
	title = db.Column(db.String)
	description = db.Column(db.Text)
	start_date = db.Column(db.DateTime, nullable=False)
	end_date = db.Column(db.DateTime, nullable=False)
	start_date_subscriptions = db.Column(db.DateTime, nullable=False)
	end_date_subscriptions = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.String, db.ForeignKey('users.id'))
	user = db.relationship('User', foreign_keys=user_id)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __init__(self, title, content, user_id):
		self.title = title
		self.content = content
		self.user_id = user_id

	def __repr__(self):
		return "{}".format(self.id, self.title, self.user)

