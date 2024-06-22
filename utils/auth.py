from functools import wraps
from flask import request, jsonify
import jwt
from config import config
from utils.db import SessionLocal
from models.user import User
import bcrypt
import datetime
from typing import Optional, Dict

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return jsonify({'message': 'Authentication required'}), 401
        with SessionLocal() as db:
            user = db.query(User).filter(User.email == auth.username).first()
            if not user or not check_password(user.password, auth.password):
                return jsonify({'message': 'Invalid credentials'}), 401
        return func(*args, **kwargs)
    return wrapper

def authorize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Authorization required'}), 401
        token = auth_header.split(" ")[1]
        try:
            decoded_token = jwt.decode(token, config.SECRET_KEY, algorithms=['HS256'])
            request.user_id = decoded_token['sub']
        except jwt.exceptions.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        return func(*args, **kwargs)
    return wrapper

def create_access_token(data: Dict, expires_delta: Optional[datetime.timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def generate_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(hashed_password: str, plain_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())