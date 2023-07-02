from init import db, ma
from marshmallow import fields
from datetime import datetime

class Incident(db.Model):
    __tablename__ = 'incidents'

    id = db.Column(db.Integer, primary_key=True)

    description = db.Column(db.Text())
    date_time = db.Column(db.DateTime, default=datetime.now)
    
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    # Defines a many-to-one relationship between the Incident and Location models.
    location = db.relationship('Location', back_populates='incidents')
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # Defines a many-to-one relationship between the Incident and User models.
    user = db.relationship('User', back_populates='incidents')

    alert_id = db.Column(db.Integer, db.ForeignKey('alerts.id'))
    # Defines a many-to-one relationship between the Incident and Alert models.
    alert = db.relationship('Alert', back_populates='incidents')

class IncidentSchema(ma.Schema):
    # Pluck field is configured to extract the id attribute from the User object
    user = fields.Pluck('UserSchema', 'id', default=None)
    # Declares a nested field for location, representing the location associated with the incident. It uses the LocationSchema for serialization.
    location = fields.Nested('LocationSchema', exclude=['incidents'])
    # Declares a nested field for alert, representing the alert associated with the incident. It uses the AlertSchema for serialization. The exclude=['incidents'] parameter excludes the incidents field from the nested serialization
    alert = fields.Nested('AlertSchema', exclude=['incidents'])

    class Meta:
        fields = ('id', 'description', 'date_time', 'location', 'alert', 'user', 'location_id', 'alert_id', 'user_id')
        ordered=True
