from flask import Flask, request
from flask_cors import CORS
from config import config
from utils.auth import authenticate, authorize, create_access_token, check_password
from routes.users import users_blueprint
from routes.predictions import predictions_blueprint
from routes.interactions import interactions_blueprint
from utils.db import Base, SessionLocal
from models.user import User
from libs.custom_response import custom_response

app = Flask(__name__)
app.config.from_object(config)
CORS(app)

# Register blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(predictions_blueprint)
app.register_blueprint(interactions_blueprint)

# Authentication and Authorization Middleware
@app.before_request
def before_request():
    authenticate(request)
    authorize(request)

# Error Handler
@app.errorhandler(401)
def unauthorized(error):
    return custom_response(error={'message': 'Unauthorized'}, status=401)

@app.errorhandler(403)
def forbidden(error):
    return custom_response(error={'message': 'Forbidden'}, status=403)

# Main Route
@app.route('/', methods=['GET'])
def index():
    return custom_response(message='DevDat.AI API')

# Authentication Endpoint
@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return custom_response(error={'message': 'Email and password are required'}, status=400)
    with SessionLocal() as db:
        user = db.query(User).filter(User.email == email).first()
        if not user or not check_password(user.password, password):
            return custom_response(error={'message': 'Invalid credentials'}, status=401)
        access_token = create_access_token(data={'sub': user.email, 'user_id': user.id})
        return custom_response({'access_token': access_token, 'user_id': user.id}, 200)

# Create Database Tables (Before Running the App)
with SessionLocal() as db:
    Base.metadata.create_all(bind=db.bind)

if __name__ == '__main__':
    app.run(debug=True) 
