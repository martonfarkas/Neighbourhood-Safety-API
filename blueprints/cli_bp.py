from flask import Blueprint
from models.user import User
from init import db, bcrypt
from datetime import datetime


cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables Created Successfully')

@cli_bp.cli.command('seed')
def seed_db():
    users = [
        User(
            name='Eric Morales',
            email='morales@spam.com',
            address='101 Hull Rd, Sydney',
            #password=bcrypt.generate_password_hash('sydney').decode('utf-8'),
            
        ),
        User(
            name='John Smith',
            email='smith@spam.com',
            address='16, Sheppards Road, Brisbane',
            #password=bcrypt.generate_password_hash('melbourne').decode('utf-8'),
        ),
        User(
            name='Sam Jones',
            email='jones@spam.com',
            address='8 Fortune Avenue, Yarra Ranges',
            #password=bcrypt.generate_password_hash('brisbane').decode('utf-8'),
        )
    ]
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()