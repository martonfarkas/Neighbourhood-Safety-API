from flask import Blueprint, request
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from flask_jwt_extended import create_access_token
from init import db, bcrypt

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/users/')
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)

@auth_bp.route('/users/<int:id>/')
def one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    return UserSchema(exclude=['password']).dump(user)

@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    try:
        user = User(
            name=request.json.get('name'),
            email=request.json['email'],
            address=request.json.get('address'),
            password=bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
            password=request.json.get('password')
        )

        db.session.add(user)
        db.session.commit()

        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'This email address already exists!'}, 409
    
@auth_bp.route('/login/', methods=['POST'])
def auth_login():
    try:
        stmt = db.select(User).filter_by(email=request.json['email'])
        user = db.session.scalar(stmt)
        if user and bcrypt.check_password_hash(user.password, request.json['password']):
            token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
            return {'token': token, 'user': UserSchema(exclude=['password']).dump(user)}
        else:
            return {'error': 'Invalid email address or password!'}, 401
    except KeyError:
        return {'error': 'Email and password are required!'}, 400