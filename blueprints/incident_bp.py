from flask import Blueprint, request
# Imports the Incident model and IncidentSchema schema from the models.incident module.
from models.incident import Incident, IncidentSchema
# Imports the datetime class from the datetime module to work with date and time values.
from datetime import datetime
# Imports the db instance, which represents the database connection.
from init import db
#  Imports the jwt_required decorator and the get_jwt_identity function from flask_jwt_extended.
from flask_jwt_extended import jwt_required

# Creates a new instance of Blueprint with the name 'incidents'
incident_bp = Blueprint('incidents', __name__, url_prefix='/incidents')

# Retrieves all incident from the database
@incident_bp.route('/', methods=['GET'])
def get_incidents():
    # Defines the get_incidents function, which handles the logic for retrieving all incidents.
    stmt = db.select(Incident).order_by(Incident.date_time.desc())
    # Constructs a SQLAlchemy select statement to retrieve all Incident records from the database and orders them by the date_time 
    incidents = db.session.scalars(stmt).all()
    return IncidentSchema(many=True).dump(incidents)

# Retrieves one incident records from the database
@incident_bp.route('/<int:incident_id>', methods=['GET'])
def one_incident(incident_id):
    # Constructs a SQLAlchemy select statement to retrieve an Incident record from the database with a matching id 
    stmt = db.select(Incident).filter_by(id=incident_id)
    # Executes the SQLAlchemy statement using the database session (db.session) and retrieves a single scalar value 
    incident = db.session.scalar(stmt)
    # Checks if an incident is found based on the incident_id.
    if incident:
        # Uses the IncidentSchema to serialize the incident into JSON-formatted data
        return IncidentSchema().dump(incident)
    else:
        return {'error': 'Incident not found'}, 404

# Create a new incident record    
@incident_bp.route('/', methods=['POST'])
@jwt_required()
def create_incident():
    # Uses the IncidentSchema to deserialize the JSON data from the request body into an incident object.
    incident_info = IncidentSchema().load(request.json)
    # : Creates a new instance of the Incident model using the deserialized data from incident_info
    incident = Incident(
        description=incident_info['description'],
        date_time=datetime.now(),
        location_id=incident_info['location_id'],
        alert_id=incident_info['alert_id'],
        user_id=incident_info['user_id'],
    )
    # Adds the newly created incident to the database session.
    db.session.add(incident)
    # Commits the changes to the database, persisting the new incident.
    db.session.commit()
    return IncidentSchema().dump(incident), 201

# Update incident from the database
@incident_bp.route('/<int:incident_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_incident(incident_id):
    # Constructs a SQLAlchemy select statement to retrieve an Incident record from the database with a matching id
    stmt = db.select(Incident).filter_by(id=incident_id)
    # Executes the SQLAlchemy statement using the database session (db.session) and retrieves a single scalar value 
    incident = db.session.scalar(stmt)
    # Uses the IncidentSchema to deserialize the JSON data from the request body into an incident object.
    incident_info = IncidentSchema().load(request.json)
    # Checks if an incident is found based on the incident_id
    if incident:
        # Updates the description of the incident with the new value from incident_info
        incident.description=incident_info['description']
        # Commits the changes to the database
        db.session.commit()
        # Uses the IncidentSchema to serialize the updated incident into JSON-formatted data and returns it.
        return IncidentSchema().dump(incident)
    else:
        return{'error': 'Incident not found'}, 404

# Delete incident from database
@incident_bp.route('/<int:incident_id>', methods=['DELETE'])
@jwt_required()
def delete_incident(incident_id):
    # Constructs a SQLAlchemy select statement to retrieve an Incident record from the database with a matching id
    stmt = db.select(Incident).filter_by(id=incident_id)
    # Executes the SQLAlchemy statement using the database session (db.session) and retrieves a single scalar value
    incident = db.session.scalar(stmt)
    # Checks if an incident is found based on the incident_id
    if incident:
        # Deletes the incident from the database session.
        db.session.delete(incident)
        #  Commits the changes to the database, deleting the incident
        db.session.commit()
        return {'message': f'Incident {incident_id} was succesfully deleted'}
    else:
        return {'error': 'Incident not found'}, 404