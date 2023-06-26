from init import db, ma

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)

    city = db.Column(db.String(50))
    address = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('Location', back_populates='location', cascade='all, delete')

class LocationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'city', 'address', 'incidents')
        ordered=True