import datetime

from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.tables import User, Event, UserEvent
from app.serializers import UserEventSchema


bp_user_event = Blueprint('user-event', __name__, url_prefix="/user-event")


@bp_user_event.route('/', methods=['get'])
# @jwt_required
def list():
    result = UserEvent.query.all()
    return UserEventSchema(many=True).jsonify(result), 200


@bp_user_event.route('/<int:id>', methods=['delete'])
def delete(id):
    user_event_exists = UserEvent.query.filter(UserEvent.id == id).first()
    if user_event_exists: 
        UserEvent.query.filter(UserEvent.id == id).delete()
        current_app.db.session.commit()
        return jsonify({
            'message': 'Removido com sucesso!.'
        }), 200
    else:
        return jsonify({
            'message': 'Registro não encontrado!.'
        }), 400


@bp_user_event.route('/<int:id>', methods=['patch'])
def update(id):
    user_event_exists = UserEvent.query.filter(UserEvent.id == id).first()
    if user_event_exists:
        user_schema = UserEventSchema()
        query = UserEvent.query.filter(UserEvent.id == id)
        query.update(request.json)
        current_app.db.session.commit()
        return user_schema.jsonify(query.first())
    else:
        return jsonify({
            'message': 'Registro não encontrado!.'
        }), 400

@bp_user_event.route('/', methods=['post'])
def create():
    user_event_schema = UserEventSchema()
    user_id = request.json["user_id"]
    event_id = request.json["event_id"]

    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({
            'message': 'Usuário não encontrado!.'
        }), 400

    event = Event.query.filter_by(id=event_id).first() 
    if not event:
        return jsonify({
            'message': 'Evento não encontrado!.'
        }), 400
    else:
        # import ipdb; ipdb.set_trace()
        # from dateutil import parser
        # dt = parser.parse(event.start_date_subscriptions)
        now = datetime.datetime.now()
        print("event.end_date_subscriptions",  event.end_date_subscriptions)

        start_date_subscriptions = datetime.datetime.timestamp(event.start_date_subscriptions)
        print("event.start_date_subscriptions", event.start_date_subscriptions)

    user_event_exists = UserEvent.query.filter_by(user_id=user_id, event_id=event_id).first()

    if not user_event_exists:
        new_user_event = UserEvent(user_id, event_id)
    else:
        return jsonify({
            'message': 'Este evento já pertence a este usuário!.'
        }), 400

    current_app.db.session.add(new_user_event)
    current_app.db.session.commit()

    return user_event_schema.jsonify(new_user_event), 201
