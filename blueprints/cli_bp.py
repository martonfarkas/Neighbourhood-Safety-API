from flask import Blueprint
from models.user import User
from models.incident import Incident
from models.location import Location
from models.alert import Alert
from init import db, bcrypt
from datetime import datetime

# Creates a Flask Blueprint named cli_bp
cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_db():
    # drops existing database tables (if any) and creates new tables based on the defined models
    db.drop_all()
    db.create_all()
    print('Tables Created Successfully')


@cli_bp.cli.command('seed')
def seed_db():
    try:
        # Delete existing data from tables
        Location.query.delete()
        User.query.delete()
        Incident.query.delete()
        Alert.query.delete()

        # Define and seed locations
        locations = [
            Location(
                city='Sydney',
                address='25 Avoca St',
            ),
            Location(
                city='Brisbane',
                address='242 Edward St',
            ),
            Location(
                city='Melbourne',
                address='19 Nelson St',
            )
        ]
        # Iterate over the locations and add them to the session
        db.session.add_all(locations)
        db.session.commit()

        # Define and seed users
        users = [
            User(
                name='Eric Morales',
                email='morales@spam.com',
                address='101 Hull Rd',
                city='Sydney',
                password=bcrypt.generate_password_hash('neighbour').decode('utf-8'),
                location=locations[0] 
            ),
            User(
                name='John Smith',
                email='smith@spam.com',
                address='16, Sheppards Road',
                city='Brisbane',
                password=bcrypt.generate_password_hash('hood').decode('utf-8'),
                location=locations[1]
            ),
            User(
                name='Sam Jones',
                email='jones@spam.com',
                address='8 Fortune Avenue',
                city='Melbourne',
                password=bcrypt.generate_password_hash('safety').decode('utf-8'),
                location=locations[2]
            )
        ]
        # Iterate over the users and add them to the session
        db.session.add_all(users)
        db.session.commit()

        # Define and seed incidents
        incidents = [
            Incident(
                description='Robbery',
                date_time=datetime.now(),
                user=users[0],
                location=locations[0]
            ),
            Incident(
                description='Burglary',
                date_time=datetime.now(),
                user=users[1],
                location=locations[1]
            ),
            Incident(
                description='Vandalism',
                date_time=datetime.now(),
                user=users[2],
                location=locations[2]
            )
        ]
        # Iterate over the incidents and add them to the session
        db.session.add_all(incidents)
        db.session.commit()

        # Define and seed alerts
        alerts = [
            Alert(
                alert_message='Alert message 1 - Robbery',
                user=users[0],
                incidents=[incidents[0]]
            ),
            Alert(
                alert_message='Alert message 2 - Burglary',
                user=users[1],
                incidents=[incidents[2]]
            ),
            Alert(
                alert_message='Alert message 3 - Vandalism',
                user=users[2],
                incidents=[incidents[1]]
            )
        ]
        # Iterate over the alerts and add them to the session
        db.session.add_all(alerts)
        db.session.commit()

        print('Models Seeded Successfully')
    except Exception as e:
        db.session.rollback()
        print(f"Seeding Error: {str(e)}")
