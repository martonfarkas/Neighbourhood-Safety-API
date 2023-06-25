from flask import Blueprint, request
from models.incident import Incident, IncidentSchema
from datetime import datetime
from init import db

incident_bp = Blueprint('incidents', __name__, url_prefix='/incidents')

@incident_bp.route('/', methods=['GET'])
def get_incidents():
    stmt = db.select(Incident).order_by(Incident.date_time.desc())
    incidents = db.session.scalars(stmt).all()
    return IncidentSchema(many=True).dump(incidents)

@incident_bp.route('/<int:incident_id>', methods=['GET'])
def one_incident(incident_id):
    stmt = db.select(Incident).filter_by(id=incident_id)
    incident = db.session.scalar(stmt)
    if incident:
        return IncidentSchema().dump(incident)
    else:
        return {'error': 'Incident not found'}, 404
    
@incident_bp.route('/', methods=['POST'])
def create_incident():
    incident_info = IncidentSchema().load(request.json)
    incident = Incident(
        description=incident_info['description'],
        date_time=datetime.now()
        # location_id=incident_info['location_id'],
        # alert_id=incident_info['alert_id'],
        # user_id=incident_info['user_id']
    )

    db.session.add(incident)
    db.session.commit()
    return IncidentSchema().dump(incident), 201

@incident_bp.route('/<int:incident_id>', methods=['PUT', 'PATCH'])
def update_incident(incident_id):
    stmt = db.select(Incident).filter_by(id=incident_id)
    incident = db.session.scalar(stmt)
    incident_info = IncidentSchema().load(request.json)
    if incident:
        incident.description=incident_info['description']
        db.session.commit()
        return IncidentSchema().dump(incident)
    else:
        return{'error': 'Incident not found'}, 404