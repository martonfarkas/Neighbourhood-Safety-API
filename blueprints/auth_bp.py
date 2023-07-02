from flask import Blueprint, request
from models.user import User, UserSchema
# IntegrityError from SQLAlchemy to handle integrity constraints
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from flask_jwt_extended import create_access_token
from init import db, bcrypt


# This blueprint will be used to define routes related to authentication.
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# # Endpoint for retrieving all users
@auth_bp.route('/users/')
def all_users():
    # # Select all users from the database
    stmt = db.select(User)
    # Retrieve all the users as scalar values
    users = db.session.scalars(stmt).all()
    # UserSchema is used to serialize the users into JSON-formatted data
    return UserSchema(many=True, exclude=['password']).dump(users)

# # Endpoint for retrieving one user by ID
@auth_bp.route('/users/<int:id>/')
def one_user(id):
    # # Select a user from the database based on the provided ID
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    # UserSchema is used to serialize the users into JSON-formatted data
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': 'User not found'}, 404

# # Endpoint for user registration
@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    try:
        # Create a new User object with the provided data
        user = User(
            name=request.json.get('name'),
            email=request.json['email'],
            city=request.json.get('city'),
            password=bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
        )
        # Add the user to the session and commit the changes to the database
        db.session.add(user)
        db.session.commit()

        # Serialize the user using UserSchema and exclude the 'password' field
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        # Return an error response if the email address already exists in the database
        return {'error': 'This email address already exists!'}, 409

# Endpoint for user login   
@auth_bp.route('/login/', methods=['POST'])
def auth_login():
    try:
        # Select a user from the database based on the provided email address
        stmt = db.select(User).filter_by(email=request.json['email'])
        user = db.session.scalar(stmt)
        if user and bcrypt.check_password_hash(user.password, request.json['password']):
            # Generate a new access token for the authenticated user
            token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
            # Return the access token and serialized user data (excluding 'password')
            return {'token': token, 'user': UserSchema(exclude=['password']).dump(user)}
        else:
            # Return an error response if the email address or password is invalid
            return {'error': 'Invalid email address or password!'}, 401
    except KeyError:
        # Return an error response if the email and password are not provided in the request
        return {'error': 'Email and password are required!'}, 400
    
