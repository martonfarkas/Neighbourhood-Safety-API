# Importing necessary dependencies
from flask import Blueprint
from models.alert import Alert, AlertSchema
from init import db

# Creating a blueprint named alert_bp with the name 'db' and the URL prefix /alerts
alert_bp = Blueprint('db', __name__, url_prefix='/alerts')

# Get all alerts
@alert_bp.route('/', methods=['GET'])
def get_alerts():
    # Retrieve all Alert records from the database, ordered by id
    stmt = db.select(Alert).order_by(Alert.id.desc())
    # Retrieve all the alerts as scalar values
    alerts = db.session.scalars(stmt).all()
    return AlertSchema(many=True).dump(alerts)

# Get a single alert
@alert_bp.route('/<int:alert_id>/', methods=['GET'])
def one_alert(alert_id):
    # Retrieve an Alert record from the database with a matching id 
    stmt = db.select(Alert).filter_by(id=alert_id)
    # Retrieve a single scalar value 
    alert = db.session.scalar(stmt)
    # If an alert is found, the AlertSchema is used to serialize the alert into JSON-formatted data
    if alert:
        return AlertSchema().dump(alert)
    else:
        return {'error': 'Alert not found'}, 404
    