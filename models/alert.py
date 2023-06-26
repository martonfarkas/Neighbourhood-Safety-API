from init import db, ma

class Alert(db.Model):
    __tablename__ = 'alerts'

    id = db.Column(db.Integer, primary_key=True)

    alert_message = db.Column(db.String())

    

class AlertSchema(ma.Schema):
    class Meta:
        fields = ('id', 'alert_message', 'user_id', 'incident_id')
        ordered=True
        