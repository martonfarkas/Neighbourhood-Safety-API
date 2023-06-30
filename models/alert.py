from init import db, ma
from marshmallow import fields
from models.user import UserSchema
from models.incident import IncidentSchema

class Alert(db.Model):
    __tablename__ = 'alerts'

    id = db.Column(db.Integer, primary_key=True)

    alert_message = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Defines a many-to-one relationship between the Alert and User models.
    user = db.relationship('User', back_populates='alerts')
    # Defines a one-to-many relationship between the Alert and Incident models.
    incidents = db.relationship('Incident', back_populates='alert', cascade='all, delete')
    

class AlertSchema(ma.Schema):
    # Declares a nested field for user, representing the user associated with the alert. It uses the UserSchema for serialization.
    user = fields.Nested(UserSchema, exclude=['alerts', 'incidents', 'location'])
    #  Declares a nested field for incidents, representing the incidents associated with the alert. It uses the IncidentSchema for serialization.
    incidents = fields.List(fields.Nested(IncidentSchema, exclude=['alert', 'user']))

    class Meta:
        fields = ('id', 'alert_message', 'user', 'incidents')
        ordered=True
        