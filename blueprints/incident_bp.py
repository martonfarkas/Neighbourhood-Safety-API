from flask import Blueprint, request
from models.incident import Incident, IncidentSchema
import datetime
from init import db

incident_bp = Blueprint('db', __name__)

@incident_bp.route('/incidents', methods=['GET'])
def get_incidents():
    stmt = db.select(Incident).order.by(Incident.status.desc())
    incidents = db.session.scalars(stmt).all()
    return IncidentSchema(many=True).dump(incidents)