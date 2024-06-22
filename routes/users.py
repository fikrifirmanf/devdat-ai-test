from flask import Blueprint, request, jsonify
from libs.custom_response import custom_response
from utils.db import SessionLocal
from models.user import User
from utils.auth import create_access_token, generate_password_hash
import bcrypt
import datetime

users_blueprint = Blueprint('users', __name__, url_prefix='/users')

@users_blueprint.route('/', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        if not email or not password:
            return custom_response(message=f'Email and password are required', status=400)
        
        hashed_password = generate_password_hash(password)
        with SessionLocal() as db:
            user = User(email=email, password=hashed_password, name=name, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
            db.add(user)
            db.commit()
            db.refresh(user)
            access_token = create_access_token(data={'sub': user.email})
            result = {'id': user.id, 'email': user.email, 'name': user.name, 'access_token': access_token, 'token_type': 'bearer'}
            return custom_response(data=result, message='User created successfully', status=201)
    except Exception as e:
        return custom_response(error=str(e), status=500)

@users_blueprint.route('/', methods=['GET'])
def get_users():
    with SessionLocal() as db:
        users = db.query(User).all()
        results = [{'id': user.id, 'email': user.email, 'name': user.name} for user in users]
        return custom_response(data=results, message='Users retrieved successfully', status=200)

@users_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            result = {'id': user.id, 'email': user.email, 'name': user.name}
            return custom_response(data=result, message='User retrieved successfully', status=200)
        else:
            return custom_response(error='User not found', status=404)

@users_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            if 'email' in data:
                user.email = data['email']
            if 'name' in data:
                user.name = data['name']
            user.updated_at = datetime.datetime.now()
            db.commit()
            return custom_response(message=f'User {user_id} updated successfully', status=200)
        else:
            return custom_response(error=f'User {user_id} not found', status=404)

@users_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return custom_response(message=f'User {user_id} deleted successfully', status=200)
        else:
            return custom_response(error=f'User {user_id} not found', status=404)