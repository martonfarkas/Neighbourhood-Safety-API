from init import db, ma


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'address', 'password')
        ordered=True