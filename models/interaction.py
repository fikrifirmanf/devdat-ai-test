from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from utils.db import Base

class Interaction(Base):
    __tablename__ = 'interactions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    prediction_id = Column(Integer, ForeignKey('predictions.id'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    data = Column(String, nullable=True) 

    def __repr__(self):
        return f"<Interaction(user_id='{self.user_id}', prediction_id='{self.prediction_id}')>"