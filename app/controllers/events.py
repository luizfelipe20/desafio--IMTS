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
    Event.query.filter(Event.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')


@bp_events.route('/<int:id>', methods=['update'])
def update(identificador):
    bs = EventSchema()
    query = Event.query.filter(Event.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())


@bp_events.route('/', methods=['post'])
def create():
    es = EventSchema()
    event, error = es.load(request.json)

    if error:
        return jsonify(error), 401

    current_app.db.session.add(event)
    current_app.db.session.commit()
    return es.jsonify(event), 201
