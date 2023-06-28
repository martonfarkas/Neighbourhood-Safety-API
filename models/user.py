from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    incidents = db.relationship('Incident', back_populates='user')
    
    alerts = db.relationship('Alert', back_populates='user')
   
    location = db.relationship('Location', back_populates='user', uselist=False)

class UserSchema(ma.Schema):
    incidents = fields.List(fields.Nested('IncidentSchema', exclude=['user']))
    location = fields.Nested('LocationSchema', exclude=['user'])
    alerts = fields.List(fields.Nested('AlertSchema', exclude=['user', 'incidents']))


    class Meta:
        fields = ('id', 'name', 'email', 'address', 'password', 'incidents', 'alerts', 'location')
        ordered=True