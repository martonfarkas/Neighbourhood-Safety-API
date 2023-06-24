from init import db, ma

class Alert(db.Model):
    __tablename__ = 'alerts'

    id = db.Column(db.Integer, primary_key=True)

    alert_message = db.Column(db.String())

    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # incidents = db.relationship('Incident', secondary='alert_incident', back_populates='alerts')

class AlertSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alert_message')
        ordered=True
        