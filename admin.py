from flask_admin import Admin

from flask_admin.contrib.pymongo import ModelView

from wtforms import fields, form


class MessageForm(form.Form):
	name = fields.StringField()
	message = fields.TextAreaField()


class MessageView(ModelView):
	form = MessageForm
	column_list = ["name"]


def configure(app):
	app.admin = Admin(app, name="Admin")
	app.admin.add_view(MessageView(app.db.message, "Messages"))