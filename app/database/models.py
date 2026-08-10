from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.database.database import Base


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    image_name = Column(String)

    emotion = Column(String)

    confidence = Column(Float)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )