from flask import Blueprint
# Imports the Location model and LocationSchema schema from the models.
from models.location import Location, LocationSchema
# Imports the db instance, which represents the database connection.
from init import db

# Creates a new instance of Blueprint with the name 'locations'
location_bp = Blueprint('locations', __name__, url_prefix='/locations')

# Decorator that associates the following function with the route /locations/ and HTTP GET method.
@location_bp.route('/', methods=['GET'])
def get_locations():
    # Constructs a SQLAlchemy select statement to retrieve all Location records from the database
    stmt = db.select(Location).order_by(Location.city.desc())
    # Executes the SQLAlchemy statement using the database session (db.session) and retrieves all locations as a list of scalar values.
    locations = db.session.scalars(stmt).all()
    return LocationSchema(many=True).dump(locations)

@location_bp.route('/<int:location_id>/', methods=['GET'])
def one_location(location_id):
    # Constructs a SQLAlchemy select statement to retrieve a Location record from the database with a matching id
    stmt = db.select(Location).filter_by(id=location_id)
    # Executes the SQLAlchemy statement using the database session (db.session) and retrieves a single scalar value 
    location = db.session.scalar(stmt)
    if location:
        return LocationSchema().dump(location)
    else:
        return {'error': 'Location not found'}, 404