from flask import Blueprint
from models.alert import Alert, AlertSchema
from init import db


alert_bp = Blueprint('db', __name__)

@alert_bp.route('/alerts', methods=['GET'])
def get_alerts():
    stmt = db.select(Alert).order_by(Alert.alert_id.desc())
    alerts = db.session.scalars(stmt).all()
    return AlertSchema(many=True).dump(alerts)