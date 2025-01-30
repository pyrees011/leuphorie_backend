from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class QuestionnaireBase(BaseModel):
    user_id: str
    question_id: int
    response: str
    created_at: datetime = datetime.utcnow()

class QuestionnaireCreate(QuestionnaireBase):
    pass

class Questionnaire(QuestionnaireBase):
    questionnaire_id: int

    class Config:
        from_attributes = True  # This enables ORM mode
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }

class QuestionnaireResponse(QuestionnaireBase):
    questionnaire_id: int

