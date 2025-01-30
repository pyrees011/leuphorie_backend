from fastapi import APIRouter, Depends
from services.questionnaireService import get_questionnaire_by_user_id_and_question_id, get_questionnaire_by_user_id, create_questionnaire as create_questionnaire_service, update_questionnaire_by_user_id_and_question_id, delete_questionnaire_by_user_id_and_question_id
from schemas.questionnaire_schema import QuestionnaireResponse, QuestionnaireCreate
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_connection import get_db
from typing import List

# utils
from utils.protected_route import authenticate

router = APIRouter()

@router.get("/questionnaire/{user_id}",response_model=list[QuestionnaireResponse], dependencies=[Depends(authenticate)])
async def get_questionnaires(user_id: str, db: AsyncSession = Depends(get_db)):
    questionnaires = await get_questionnaire_by_user_id(user_id, db)
    return questionnaires

@router.get("/questionnaire/{user_id}/{question_id}", response_model=QuestionnaireResponse, dependencies=[Depends(authenticate)])
async def get_questionnaire_by_id(user_id: str, question_id: int, db: AsyncSession = Depends(get_db)):
    return await get_questionnaire_by_user_id_and_question_id(user_id, question_id, db)

@router.post("/questionnaire", response_model=QuestionnaireResponse, dependencies=[Depends(authenticate)])
async def create_questionnaire(questionnaire: QuestionnaireCreate, db: AsyncSession = Depends(get_db)):
    return await create_questionnaire_service(questionnaire, db)

@router.put("/questionnaire/{user_id}/{question_id}", response_model=QuestionnaireResponse, dependencies=[Depends(authenticate)])
async def update_questionnaire(user_id: str, question_id: int, questionnaire: QuestionnaireCreate, db: AsyncSession = Depends(get_db)):
    return await update_questionnaire_by_user_id_and_question_id(user_id, question_id, questionnaire, db)

@router.delete("/questionnaire/{user_id}/{question_id}", response_model=QuestionnaireResponse, dependencies=[Depends(authenticate)])
async def delete_questionnaire(user_id: str, question_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_questionnaire_by_user_id_and_question_id(user_id, question_id, db)