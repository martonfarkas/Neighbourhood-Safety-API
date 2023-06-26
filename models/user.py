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
    alerts = db.relationship('Alert', secondary='incidents', back_populates='user', cascade='all, delete')

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'address', 'password', 'incidents', 'alerts')
        ordered=True