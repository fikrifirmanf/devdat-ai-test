from sqlalchemy import Column, Float, Integer, ForeignKey, String, DateTime
from utils.db import Base

class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    image_url = Column(String, nullable=False)
    prediction_label = Column(String, nullable=False)
    prediction = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Prediction(image_url='{self.image_url}', prediction='{self.prediction}')>"