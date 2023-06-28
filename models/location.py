from init import db, ma
from marshmallow import fields

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)

    city = db.Column(db.String(50))
    address = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)

    user = db.relationship('User', back_populates='location')
    incidents = db.relationship('Incident', back_populates='location')

class LocationSchema(ma.Schema):
    incidents = fields.List(fields.Nested('IncidentSchema', exclude=['location']))
    user = fields.Nested('UserSchema', exclude=['location', 'incidents'])
    class Meta:
        fields = ('id', 'city', 'address', 'incidents', 'user')
        ordered=True