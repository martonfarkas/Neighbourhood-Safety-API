from flask import Blueprint
from models.location import Location, LocationSchema
from init import db

location_bp = Blueprint('locations', __name__, url_prefix='/locations')

@location_bp.route('', methods=['GET'])
def get_locations():
    stmt = db.select(Location).order_by(Location.city.desc())
    locations = db.session.scalars(stmt).all()
    return LocationSchema(many=True).dump(locations)

@location_bp.route('/<int:location_id>/', methods=['GET'])
def one_location(location_id):
    stmt = db.select(Location).filter_by(id=location_id)
    location = db.session.scalar(stmt)
    if location:
        return LocationSchema().dump(location)
    else:
        return {'error': 'Location not found'}, 404