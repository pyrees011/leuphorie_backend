from models.questionnaire import Questionnaire
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_questionnaire_by_id(questionnaire_id: int, db: AsyncSession):
    questionnaire = await db.execute(select(Questionnaire).where(Questionnaire.id == questionnaire_id))
    return questionnaire.scalar_one_or_none()
    
async def get_questionnaire_by_name(name: str, db: AsyncSession):
    questionnaire = await db.execute(select(Questionnaire).where(Questionnaire.name == name))
    return questionnaire.scalar_one_or_none()
    
async def create_questionnaire(questionnaire: Questionnaire, db: AsyncSession):
    db.add(questionnaire)
    await db.commit()
    await db.refresh(questionnaire)
    return questionnaire
    
async def update_questionnaire(questionnaire: Questionnaire, db: AsyncSession):
    db.merge(questionnaire)
    await db.commit()
    await db.refresh(questionnaire)
    return questionnaire
    
async def delete_questionnaire(questionnaire_id: int, db: AsyncSession):
    questionnaire = await db.execute(select(Questionnaire).where(Questionnaire.id == questionnaire_id))
    if questionnaire:
        await db.delete(questionnaire)
        await db.commit()
    return questionnaire
