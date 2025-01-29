from pydantic import BaseModel
from datetime import datetime

class QuestionnaireCreate(BaseModel):
    user_id: int
    question_id: int
    response: str

class QuestionnaireResponse(BaseModel):
    questionnaire_id: int
    user_id: int
    question_id: int
    response: str
    created_at: datetime

    class Config:
        orm_mode = True
