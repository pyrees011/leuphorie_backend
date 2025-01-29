from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from db.db_connection import Base

class Questionnaire(Base):
    __tablename__ = "questionnaires"

    questionnaire_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, nullable=False)
    response = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
