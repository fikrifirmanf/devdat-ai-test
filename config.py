import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'fikri20244202')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///devdat.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MODEL_FILE = 'tf_based_model.ipynb'  #  Now points to the notebook inside utils folder

    # For Google/Microsoft SSO:
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    MICROSOFT_CLIENT_ID = os.getenv('MICROSOFT_CLIENT_ID')
    MICROSOFT_CLIENT_SECRET = os.getenv('MICROSOFT_CLIENT_SECRET')

config = Config()