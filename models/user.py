from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    incidents = db.relationship('Incident', back_populates='user', cascade='all, delete')
    alerts = db.relationship('Alert', back_populates='user', cascade='all, delete')
    location = db.relationship('Location', back_populates='user', uselist=False, cascade='all, delete')

class UserSchema(ma.Schema):
    incidents = fields.List(fields.Nested('IncidentSchema', exclude=['user', 'id']))
    class Meta:
        fields = ('name', 'email', 'address', 'password', 'incidents')
        ordered=True