from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.tables import Event
from app.serializers import EventSchema


bp_events = Blueprint('event', __name__, url_prefix="/event")


@bp_events.route('/', methods=['GET'])
# @jwt_required
def list():
    result = Event.query.all()
    return EventSchema(many=True).jsonify(result), 200


@bp_events.route('/<int:id>', methods=['delete'])
def delete(id):
    event_exists = Event.query.filter(Event.id == id).first()
    if event_exists: 
        Event.query.filter(Event.id == id).delete()
        current_app.db.session.commit()
        return jsonify('Deletado!!!!')
    else:
        return jsonify({
            'message': 'Registro não encontrado!.'
        }), 400

    
@bp_events.route('/<int:id>', methods=['update'])
def update(identificador):
    event_exists = Event.query.filter(Event.id == id).first()
    if event_exists: 
        event_schema = EventSchema()
        query = Event.query.filter(Event.id == id)
        query.update(request.json)
        current_app.db.session.commit()
        return event_schema.jsonify(query.first())
    else:
        return jsonify({
            'message': 'Registro não encontrado!.'
        }), 400


@bp_events.route('/', methods=['post'])
def create():
    event_schema = EventSchema()    
    username = request.json["username"]
    password = request.json["password"]
    
    event_exists = Event.query.filter_by(username=username).first()

    if not event_exists:
        new_event = Event(username, password)
    else:
        return jsonify({
            'message': 'Este evento já foi registrado!.'
        }), 400

    current_app.db.session.add(new_event)
    current_app.db.session.commit()

    return event_schema.jsonify(new_event), 201
