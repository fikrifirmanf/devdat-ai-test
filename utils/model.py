import json
import numpy as np
import tensorflow as tf
import os

def load_model():
    """Loads a pre-trained TensorFlow model from an .h5 file.

    Returns:
        tf.keras.Model: The loaded model.
    """
    model_path = os.path.join(os.path.dirname(__file__), 'ml_model/model', 'best_plant_disease.h5')
    print(f"Model path: {model_path}")  # Print the model path for verification
    try:
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Make Prediction
def predict(image_data, model):
    """Makes predictions using the loaded model.

    Args:
        image_data: The input image data (should be a NumPy array).
        model: The loaded TensorFlow model.

    Returns:
        The model's predictions.
    """
    if model is None:
        print("Model loading failed. Cannot make predictions.")
        return None

    # Validate input data type
    if not isinstance(image_data, tf.Tensor):
        print("Invalid input data type. Expected a NumPy array.")
        return None

    # Preprocess image data
    prediction = model.predict(image_data)
    label = cast_label(np.argmax(prediction))

    return prediction, label

def cast_label(result):
    encoder_path = os.path.join(os.path.dirname(__file__), 'ml_model/dataset', 'labelEncoder_dict.json')

    with open(encoder_path, 'r') as file:
        labels = json.load(file)

    for key, value in labels.items():
        if str(result) == key:
            return value
