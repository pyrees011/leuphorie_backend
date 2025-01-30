from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from db.db_connection import Base

class Questionnaire(Base):
    __tablename__ = "questionnaire"

    questionnaire_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    question_id = Column(Integer, index=True)
    response = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)