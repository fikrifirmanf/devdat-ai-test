from flask import Blueprint, request, jsonify
from libs.custom_response import custom_response
from utils.db import SessionLocal
from models.interaction import Interaction

interactions_blueprint = Blueprint('interactions', __name__, url_prefix='/interactions')

@interactions_blueprint.route('/', methods=['GET'])
def get_interactions():
    with SessionLocal() as db:
        interactions = db.query(Interaction).all()
        results = [{'id': interaction.id, 'user_id': interaction.user_id, 'prediction_id': interaction.prediction_id, 'timestamp': interaction.timestamp, 'data': interaction.data} for interaction in interactions]
        return custom_response(data=results, status=200, message='success')

@interactions_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user_interactions(user_id):
    with SessionLocal() as db:
        interactions = db.query(Interaction).filter(Interaction.user_id == user_id).all()
        results = [{'id': interaction.id, 'prediction_id': interaction.prediction_id, 'timestamp': interaction.timestamp, 'data': interaction.data} for interaction in interactions]
        return custom_response(data=results, status=200, message='success')

@interactions_blueprint.route('/<int:prediction_id>', methods=['GET'])
def get_prediction_interactions(prediction_id):
    with SessionLocal() as db:
        interactions = db.query(Interaction).filter(Interaction.prediction_id == prediction_id).all()
        results = [{'id': interaction.id, 'user_id': interaction.user_id, 'timestamp': interaction.timestamp, 'data': interaction.data} for interaction in interactions]
        return custom_response(data=results, status=200, message='success')