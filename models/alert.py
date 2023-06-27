from init import db, ma
from marshmallow import fields
from models.user import UserSchema
from models.incident import IncidentSchema

class Alert(db.Model):
    __tablename__ = 'alerts'

    id = db.Column(db.Integer, primary_key=True)

    alert_message = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='alerts')
    
    incidents = db.relationship('Incident', back_populates='alert', cascade='all, delete')
    

class AlertSchema(ma.Schema):
    user = fields.Nested(UserSchema, exclude=['alerts'])
    incidents = fields.Nested(IncidentSchema, exclude=['alert'], many=True)

    class Meta:
        fields = ('id', 'alert_message', 'user', 'incidents')
        ordered=True
        