from models.questionnaire import Questionnaire
from schemas.questionnaire_schema import QuestionnaireCreate, QuestionnaireResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_questionnaire_by_user_id_and_question_id(user_id: str, question_id: int, db: AsyncSession):
    questionnaire = await db.execute(select(Questionnaire).where(Questionnaire.user_id == user_id, Questionnaire.question_id == question_id))
    return questionnaire.scalar_one_or_none()
    
async def get_questionnaire_by_user_id(user_id: str, db: AsyncSession):
    query = select(Questionnaire).where(Questionnaire.user_id == user_id)
    result = await db.execute(query)
    questionnaires = result.scalars().all()
    return questionnaires
    
async def create_questionnaire(questionnaire: QuestionnaireCreate, db: AsyncSession):
    db_questionnaire = Questionnaire(**questionnaire.model_dump())
    db.add(db_questionnaire)
    await db.commit()
    await db.refresh(db_questionnaire)
    return db_questionnaire
    
async def update_questionnaire_by_user_id_and_question_id(user_id: str, question_id: int, questionnaire: Questionnaire, db: AsyncSession):
    result = await db.execute(select(Questionnaire).where(Questionnaire.user_id == user_id, Questionnaire.question_id == question_id))
    if result:
        result.update(questionnaire)
        await db.commit()
        await db.refresh(questionnaire)
    return questionnaire
    
async def delete_questionnaire_by_user_id_and_question_id(user_id: str, question_id: int, db: AsyncSession):
    questionnaire = await db.execute(select(Questionnaire).where(Questionnaire.user_id == user_id, Questionnaire.question_id == question_id))
    if questionnaire:
        await db.delete(questionnaire)
        await db.commit()
    return questionnaire
