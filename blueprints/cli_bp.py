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
    try:
        locations = [
            Location(
                city='Sydney',
                address='25 Avoca St, Randwick',
            ),
            Location(
                city='Brisbane',
                address='242 Edward St, Brisbane City',
            ),
            Location(
                city='Melbourne',
                address='19 Nelson St, Maroondah',
            )
        ]
        for location in locations:
            if location.city and location.address:
                db.session.add_all([location])
            else:
                print(f"Invalid data for location: {location}")
        #db.session.query(Location).delete()
        #db.session.add_all(locations)
        db.session.commit()

        users = [
            User(
                name='Eric Morales',
                email='morales@spam.com',
                address='101 Hull Rd, Sydney',
                password=bcrypt.generate_password_hash('neighbour').decode('utf-8'),
                location=locations[0] 
            ),
            User(
                name='John Smith',
                email='smith@spam.com',
                address='16, Sheppards Road, Brisbane',
                password=bcrypt.generate_password_hash('hood').decode('utf-8'),
                location=locations[1]
            ),
            User(
                name='Sam Jones',
                email='jones@spam.com',
                address='8 Fortune Avenue, Melbourne',
                password=bcrypt.generate_password_hash('safety').decode('utf-8'),
                location=locations[2]
            )
        ]
        for user in users:
            if user.name and user.email and user.address and user.password:
                db.session.add_all([user])
            else:
                print(f"Invalid data for user: {user}")
        #db.session.query(User).delete()
        #db.session.add_all(users)
        db.session.commit()

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
        for incident in incidents:
            if incident.description and incident.date_time and incident.user and incident.location:
                db.session.add_all([incident])
            else:
                print(f"Invalid data for incident: {incident}")
        #db.session.query(Incident).delete()
        #db.session.add_all(incidents)
        db.session.commit()

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
        for alert in alerts:
            print(f"Alert Message: {alert.alert_message}")
            print(f"User: {alert.user}")
            print(f"Incidents: {alert.incidents}")
            if alert.alert_message and alert.user and alert.incidents:
                db.session.add(alert)
                alert.incidents = alert.incidents 
                db.session.add(alert)
                
                # db.session.add([alert])
                # db.session.add_all(alert.incidents)
            else:
                print(f"Invalid data for alert: {alert}")
        #db.session.query(Alert).delete()
        #db.session.add_all(alerts)
        db.session.commit()

        print('Models Seeded Successfully')
    except Exception as e:
        db.session.rollback()
        print(f"Seeding Error: {str(e)}")
