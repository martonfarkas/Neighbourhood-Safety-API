from init import db, ma
from marshmallow import fields
from datetime import datetime

class Incident(db.Model):
    __tablename__ = 'incidents'

    id = db.Column(db.Integer, primary_key=True)

    description = db.Column(db.Text())
    date_time = db.Column(db.DateTime, default=datetime.now)

    # alert_id = db.Column(db.Integer, db.ForeignKey('alerts.id'))
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    # location = db.relationship('Location', uselist=False, back_populates='incidents', cascade='all, delete')

class IncidentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description', 'date_time')
        ordered=True