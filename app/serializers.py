from marshmallow import fields, validates, ValidationError, post_load
from flask_marshmallow import Marshmallow
from app.models.tables import User, Event, UserEvent

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class EventSchema(ma.ModelSchema):
    class Meta:
        model = Event

    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    start_date_subscriptions = fields.DateTime(required=True)
    end_date_subscriptions = fields.DateTime(required=True)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserEventSchema(ma.ModelSchema):
    class Meta:
        model = UserEvent

    user_id = fields.Integer(required=True)
    event_id = fields.Integer(required=True)