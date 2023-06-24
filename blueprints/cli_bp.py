from flask import Blueprint
from models.user import User
from models.incident import Incident
from models.location import Location
from models.alert import Alert
from init import db, bcrypt
from datetime import datetime


cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables Created Successfully')

@cli_bp.cli.command('seed')
def seed_db():
    users = [
        User(
            name='Eric Morales',
            email='morales@spam.com',
            address='101 Hull Rd, Sydney',
            password='abc',
            
        ),
        User(
            name='John Smith',
            email='smith@spam.com',
            address='16, Sheppards Road, Brisbane',
            password='bca',
        ),
        User(
            name='Sam Jones',
            email='jones@spam.com',
            address='8 Fortune Avenue, Yarra Ranges',
            password='cab',
        )
    ]
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

    incidents = [
        Incident(
            description='Robbery',
            date_time=datetime.now(),
            #user=users[0],
        ),
         Incident(
            description='Burglary',
            date_time=datetime.now(),
            #user=users[1],
        ),
         Incident(
            description='Vandalism',
            date_time=datetime.now(),
            #user=users[1],
        )
    ]
    db.session.query(Incident).delete()
    db.session.add_all(incidents)
    db.session.commit()

    locations = [
        Location(
            city='Sydney',
            address='25 Avoca St, Randwick'
        ),
        Location(
            city='Brisbane',
            address='242 Edward St, Brisbane City'
        ),
        Location(
            city='Melbourne',
            address='19 Nelson St, Maroondah'
        )
    ]
    db.session.query(Location).delete()
    db.session.add_all(locations)
    db.session.commit()

    alerts = [
        Alert(
            alert_message='Alert message 1 - Robbery'
        ),
        Alert(
            alert_message='Alert message 2 - Burglary'
        ),
        Alert(
            alert_message='Alert message 3 - Vandalism'
        )
    ]
    db.session.query(Alert).delete()
    db.session.add_all(alerts)
    db.session.commit()

    print('Models Seeded Successfully')
