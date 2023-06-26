from init import db, ma
from marshmallow import fields
from datetime import datetime

class Incident(db.Model):
    __tablename__ = 'incidents'

    id = db.Column(db.Integer, primary_key=True)

    description = db.Column(db.Text())
    date_time = db.Column(db.DateTime, default=datetime.now)

    
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    location = db.relationship('Location', back_populates='incidents', cascade='all, delete')
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='incidents')

    alert_id = db.Column(db.Integer, db.ForeignKey('alerts.id'))
    alert = db.relationship('Alert', back_populates='incidents')

class IncidentSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password', 'incidents'])
    class Meta:
        fields = ('id', 'description', 'date_time', 'user')
        ordered=True