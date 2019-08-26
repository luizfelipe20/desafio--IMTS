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
        return jsonify({
            'message': 'Removido com sucesso!.'
        }), 200
    else:
        return jsonify({
            'message': 'Registro não encontrado!.'
        }), 400

    
@bp_events.route('/<int:id>', methods=['patch'])
def update(id):
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
    title = request.json["title"]
    description = request.json["description"]
    start_date = request.json["start_date"]
    end_date = request.json["end_date"]
    start_date_subscriptions = request.json["start_date_subscriptions"]
    end_date_subscriptions = request.json["end_date_subscriptions"]
    user_id = request.json["user_id"]
    
    event_exists = Event.query.filter_by(
        title=title,
        start_date=start_date,
        end_date=end_date,
        start_date_subscriptions=start_date_subscriptions,
        end_date_subscriptions=end_date_subscriptions,
        user_id=user_id
    ).first()

    if not event_exists:
        new_event = Event(
            title, 
            description, 
            start_date, 
            end_date, 
            start_date_subscriptions, 
            end_date_subscriptions,
            user_id
        )
    else:
        return jsonify({
            'message': 'Este evento já foi registrado!.'
        }), 400

    current_app.db.session.add(new_event)
    current_app.db.session.commit()

    return event_schema .jsonify(new_event), 201
