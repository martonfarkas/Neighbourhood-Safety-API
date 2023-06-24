from flask import Blueprint
from models.location import Location, LocationSchema
from init import db

location_bp = Blueprint('db', __name__)

@location_bp.route('/locations', methods=['GET'])
def get_locations():
    stmt = db.select(Location).order_by(Location.city.desc())
    locations = db.session.scalars(stmt).all()
    return LocationSchema(many=True).dump(locations)