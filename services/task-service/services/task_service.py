from db.mongodb import task_collection
from models.task import TaskCategory, TaskItem, TaskCategoryCreate, TaskItemCreate
from bson import ObjectId
from datetime import datetime

async def create_category(user_id: str, category: TaskCategoryCreate):
    category_dict = {
        "user_id": user_id,
        "name": category.name,
        "tasks": [],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    result = await task_collection.insert_one(category_dict)
    created_category = await task_collection.find_one({"_id": result.inserted_id})
    return TaskCategory(**created_category)

async def get_all_categories(user_id: str):
    categories = []
    cursor = task_collection.find({"user_id": user_id})
    async for document in cursor:
        categories.append(TaskCategory(**document))
    return categories

async def get_category(user_id: str, category_id: str):
    category = await task_collection.find_one({"_id": ObjectId(category_id), "user_id": user_id})
    if category:
        return TaskCategory(**category)
    return None

async def add_task_to_category(user_id: str, category_id: str, task: TaskItemCreate):
    task_dict = {
        "_id": ObjectId(),
        **task.model_dump(),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    
    result = await task_collection.update_one(
        { "_id": ObjectId(category_id), "user_id": user_id },
        {
            "$push": {"tasks": task_dict},
            "$set": {"updated_at": datetime.utcnow()}
        }
    )
    if result.modified_count:
        return await get_category(user_id, category_id)
    return None

async def update_task_status(user_id: str, category_id: str, task_id: str, new_status: str):
    result = await task_collection.update_one(
        {
            "_id": ObjectId(category_id),
            "tasks._id": ObjectId(task_id),
            "user_id": user_id
        },
        {
            "$set": {
                "tasks.$.status": new_status,
                "tasks.$.updated_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        }
    )
    if result.modified_count:
        return await get_category(user_id, category_id)
    return None

async def delete_task(user_id: str, category_id: str, task_id: str):
    result = await task_collection.update_one(
        { "_id": ObjectId(category_id), "user_id": user_id },
        {
            "$pull": {"tasks": {"_id": ObjectId(task_id)}},
            "$set": {"updated_at": datetime.utcnow()}
        }
    )
    if result.modified_count:
        return await get_category(user_id, category_id)
    return None

async def delete_category(user_id: str, category_id: str):
    result = await task_collection.delete_one({"_id": ObjectId(category_id), "user_id": user_id })
    return result.deleted_count > 0 