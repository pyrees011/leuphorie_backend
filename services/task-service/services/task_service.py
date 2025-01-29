from db.mongodb import task_collection
from models.task import TaskCategory, TaskItem, TaskCategoryCreate, TaskItemCreate
from bson import ObjectId
from datetime import datetime

async def create_category(category: TaskCategoryCreate):
    category_dict = {
        "name": category.name,
        "tasks": [],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    result = await task_collection.insert_one(category_dict)
    created_category = await task_collection.find_one({"_id": result.inserted_id})
    print(created_category)
    return TaskCategory(**created_category)

async def get_all_categories():
    categories = []
    cursor = task_collection.find()
    async for document in cursor:
        categories.append(TaskCategory(**document))
    return categories

async def get_category(category_id: str):
    category = await task_collection.find_one({"_id": ObjectId(category_id)})
    if category:
        return TaskCategory(**category)
    return None

async def add_task_to_category(category_id: str, task: TaskItemCreate):
    task_dict = {
        "_id": ObjectId(),
        **task.model_dump(),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    
    result = await task_collection.update_one(
        {"_id": ObjectId(category_id)},
        {
            "$push": {"tasks": task_dict},
            "$set": {"updated_at": datetime.utcnow()}
        }
    )
    if result.modified_count:
        return await get_category(category_id)
    return None

async def update_task_status(category_id: str, task_id: str, new_status: str):
    result = await task_collection.update_one(
        {
            "_id": ObjectId(category_id),
            "tasks._id": ObjectId(task_id)
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
        return await get_category(category_id)
    return None

async def delete_task(category_id: str, task_id: str):
    result = await task_collection.update_one(
        {"_id": ObjectId(category_id)},
        {
            "$pull": {"tasks": {"_id": ObjectId(task_id)}},
            "$set": {"updated_at": datetime.utcnow()}
        }
    )
    if result.modified_count:
        return await get_category(category_id)
    return None

async def delete_category(category_id: str):
    result = await task_collection.delete_one({"_id": ObjectId(category_id)})
    return result.deleted_count > 0 