# The code imports necessary modules and classes from Flask, OS, and other files/modules.
# It also imports blueprints and exception classes required for the application
from flask import Flask
from os import environ
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp
from blueprints.alert_bp import alert_bp
from blueprints.incident_bp import incident_bp
from blueprints.location_bp import location_bp
from marshmallow.exceptions import ValidationError

# Defines a function named create_app() that creates a Flask application instance
def create_app():
    app = Flask(__name__)

    # Uses the environment variables DB_URI and JWT_KEY to configure the SQLAlchemy database URI and JWT secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
    
    # Initializes the Flask extensions (SQLAlchemy, Marshmallow, JWTManager, Bcrypt) with the Flask application instance
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Error handlers. These functions are executed when the corresponding error occurs
    @app.errorhandler(404)
    def not_found(err): 
        return {'error': str(err)}, 404
    
    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)}, 400
    
    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': 'You must be admin to do that!'}, 401
    
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages}, 400
    
    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is missing'}, 400

    # Registers the defined blueprints
    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp, name='auth_bp')
    app.register_blueprint(alert_bp, name='alert_bp')
    app.register_blueprint(incident_bp, name='incident_bp')
    app.register_blueprint(location_bp, name='location_bp')
    
    # Returns the created Flask application instance
    return app