from init import db, ma
from marshmallow import fields

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)

    city = db.Column(db.String(50))
    address = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)

    # Defines a many-to-one relationship between the Location and User models.
    user = db.relationship('User', back_populates='location')
    # Defines a one-to-many relationship between the Location and Incident models.
    incidents = db.relationship('Incident', back_populates='location')

class LocationSchema(ma.Schema):
    # Declares a nested field for incidents, representing a list of incidents associated with the location. It uses the UserSchema for serialization.
    incidents = fields.List(fields.Nested('IncidentSchema', exclude=['location', 'user']))
    
    # Declares a nested field for user, representing the user associated with the location. It uses the UserSchema for serialization.
    #user = fields.Nested('UserSchema', only=['id', 'name', 'email'], exclude=['location', 'incidents', 'password'])
    
    user = fields.Pluck('UserSchema', 'id', default=None)
    class Meta:
        fields = ('id', 'city', 'address', 'incidents', 'user')
        ordered=True
