from flask import Flask
from os import environ
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp
from blueprints.alert_bp import alert_bp
from blueprints.incident_bp import incident_bp
from blueprints.location_bp import location_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')

db.init_app(app)
ma.init_app(app)
jwt.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(cli_bp, name='cli_bp')
app.register_blueprint(auth_bp, name='auth_bp')
app.register_blueprint(alert_bp, name='alert_bp')
app.register_blueprint(incident_bp, name='incident_bp')
app.register_blueprint(location_bp, name='location_bp')

