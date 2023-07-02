from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String)
    password = db.Column(db.String, nullable=False)

    # Defines a one-to-many relationship between User and Incident models, where a user can have multiple incidents.
    incidents = db.relationship('Incident', back_populates='user')
    # Defines a one-to-many relationship between User and Alert models, where a user can have multiple alerts.
    alerts = db.relationship('Alert', back_populates='user')
    # Defines a one-to-one relationship between User and Location models, where a user can have only one location.
    location = db.relationship('Location', back_populates='user', uselist=False)

class UserSchema(ma.Schema):
    # Declares a nested field for incidents, representing a list of incidents associated with the user. It uses the IncidentSchema for serialization.
    incidents = fields.List(fields.Nested('IncidentSchema', exclude=['user', 'location']))
    # Declares a nested field for location, representing the user's location. It uses the LocationSchema for serialization.
    location = fields.Nested('LocationSchema', exclude=['user'])
    # Declares a nested field for alerts, representing a list of alerts associated with the user. It uses the AlertSchema for serialization.
    alerts = fields.List(fields.Nested('AlertSchema', only=['id', 'alert_message'], exclude=['user', 'incidents']))

    class Meta:
        fields = ('id', 'password', 'name', 'email', 'address', 'city', 'incidents', 'alerts', 'location')
        ordered=True