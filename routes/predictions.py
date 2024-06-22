from flask import Blueprint, request, jsonify
from libs.custom_response import custom_response
from utils.db import SessionLocal
from models.prediction import Prediction
from models.interaction import Interaction
from utils.image_utils import validate_image, process_image
from utils.model import load_model, predict
import os
import datetime

predictions_blueprint = Blueprint('predictions', __name__, url_prefix='/predictions')

@predictions_blueprint.route('/', methods=['POST'])
def create_prediction():
    user_id = request.form.get('user_id')
    image_file = request.files.get('image')
    if not user_id or not image_file:
        return jsonify({'message': 'User ID and Image are required'}), 400

    if not validate_image(image_file.filename):
        return jsonify({'message': 'Invalid image format. Only JPG/PNG allowed'}), 400

    # Save Image Locally
    image_path = os.path.join('uploads', image_file.filename)
    os.makedirs('uploads', exist_ok=True)  # Create uploads directory if it doesn't exist
    image_file.save(image_path) 

    # Process Image
    image_data = process_image(image_path)

    # Load Model
    model = load_model()

    # Make Prediction
    prediction_raw_data, label = predict(image_data, model)
    prediction_list = prediction_raw_data.tolist()

    # Save Prediction to Database
    with SessionLocal() as db:
        prediction = Prediction(
            user_id=user_id,
            image_url=f"/uploads/{image_file.filename}",
            prediction=str(prediction_list),
            prediction_label=str(label),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        db.add(prediction)
        db.commit()
        db.refresh(prediction)

        interaction = Interaction(
            user_id=user_id,
            prediction_id=prediction.id,
            timestamp=datetime.datetime.now(),
            data=f'Image uploaded: {image_file.filename}'
        )
        db.add(interaction)
        db.commit()
        db.refresh(interaction)

        return custom_response(message='Prediction created successfully', status=201)

@predictions_blueprint.route('/', methods=['GET'])
def get_predictions():
    with SessionLocal() as db:
        predictions = db.query(Prediction).all()
        results = [{'id': prediction.id, 'image_url': prediction.image_url, 'prediction_label': prediction.prediction_label, 'prediction': prediction.prediction} for prediction in predictions]
        return custom_response(data=results, message='Predictions retrieved successfully', status=200)

@predictions_blueprint.route('/<int:prediction_id>', methods=['GET'])
def get_prediction(prediction_id):
    with SessionLocal() as db:
        prediction = db.query(Prediction).filter(Prediction.id == prediction_id).first()
        if prediction:
            result = {'id': prediction.id, 'image_url': prediction.image_url, 'prediction_label': prediction.prediction_label, 'prediction': prediction.prediction}
            return custom_response(data=result, message='Prediction retrieved successfully', status=200)
        else:
            return custom_response(error={'message' : 'Prediction not found'}, status=404)

@predictions_blueprint.route('/<int:prediction_id>', methods=['DELETE'])
def delete_prediction(prediction_id):
    with SessionLocal() as db:
        prediction = db.query(Prediction).filter(Prediction.id == prediction_id).first()
        if prediction:
            db.delete(prediction)
            db.commit()
            return custom_response(message='Prediction deleted successfully')
        else:
            return custom_response(error={'message' : 'Prediction not found'}, status=404)