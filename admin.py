from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView

from wtforms import fields, form


class MessageForm(form.Form):
	name = fields.StringField()
	message = fields.TextAreaField()


class MessageView(ModelView):
	form = fields.StringField()
	column_list = ["name"]


def configure(app):
	app.admin = Admin(app, name="Admin")
	app.admin.add_view(MessageView(app.db.messages, "Messages"))