from fastapi import APIRouter, Depends
from services.questionnaireService import get_questionnaire_by_id, get_questionnaire_by_name, create_questionnaire, update_questionnaire, delete_questionnaire
from schemas.questionnaire_schema import QuestionnaireResponse, QuestionnaireCreate
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_connection import get_db

# utils
from utils.protected_route import authenticate

router = APIRouter()

@router.get("/questionnaires",response_model=list[QuestionnaireResponse], dependencies=[Depends(authenticate)])
async def get_questionnaires(db: AsyncSession = Depends(get_db)):
    return await get_questionnaires(db)

@router.get("/questionnaires/{questionnaire_id}", response_model=QuestionnaireResponse, dependencies=[Depends(authenticate)])
async def get_questionnaire_by_id(questionnaire_id: int, db: AsyncSession = Depends(get_db)):
    return await get_questionnaire_by_id(questionnaire_id, db)

@router.post("/questionnaires", response_model=QuestionnaireResponse, dependencies=[Depends(authenticate)])
async def create_questionnaire(questionnaire: QuestionnaireCreate, db: AsyncSession = Depends(get_db)):
    return await create_questionnaire(questionnaire, db)

@router.put("/questionnaires/{questionnaire_id}", response_model=QuestionnaireResponse, dependencies=[Depends(authenticate)])
async def update_questionnaire(questionnaire_id: int, questionnaire: QuestionnaireCreate, db: AsyncSession = Depends(get_db)):
    return await update_questionnaire(questionnaire_id, questionnaire, db)

@router.delete("/questionnaires/{questionnaire_id}", response_model=QuestionnaireResponse, dependencies=[Depends(authenticate)])
async def delete_questionnaire(questionnaire_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_questionnaire(questionnaire_id, db)