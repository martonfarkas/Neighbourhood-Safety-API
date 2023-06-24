from init import db, ma

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)

    city = db.Column(db.String(50))
    address = db.Column(db.String(100))

    incident = db.relationship('Incident', uselist=False, back_populates='location')

class LocationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'city', 'address')
        ordered=True