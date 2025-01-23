from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.core.db import Base
from datetime import datetime

class Response(Base):
    __tablename__ = "responses"

    response_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, nullable=False)
    response = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
