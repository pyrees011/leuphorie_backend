from fastapi import APIRouter, HTTPException, Depends, Request, Body
from models.task import TaskCategory, TaskCategoryCreate, TaskItemCreate
from services.task_service import (
    create_category,
    get_all_categories,
    get_category,
    add_task_to_category,
    update_task_status,
    delete_task,
    delete_category
)
from utils.protected_route import authenticate

router = APIRouter()

@router.post("/categories", response_model=TaskCategory, dependencies=[Depends(authenticate)])
async def create_new_category(category: TaskCategoryCreate):
    return await create_category(category)

@router.get("/categories", response_model=list[TaskCategory], dependencies=[Depends(authenticate)])
async def list_categories():
    return await get_all_categories()

@router.get("/categories/{category_id}", response_model=TaskCategory, dependencies=[Depends(authenticate)])
async def get_single_category(category_id: str):
    category = await get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/categories/{category_id}/tasks", response_model=TaskCategory, dependencies=[Depends(authenticate)])
async def add_task(category_id: str, task: TaskItemCreate):
    result = await add_task_to_category(category_id, task)
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return result

@router.patch("/categories/{category_id}/tasks/{task_id}/status", response_model=TaskCategory, dependencies=[Depends(authenticate)])
async def update_task_status_endpoint(
    category_id: str, 
    task_id: str, 
    status: str = Body(..., embed=True)
):
    if status not in ["todo", "inProgress", "reviewing", "done"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    result = await update_task_status(category_id, task_id, status)
    if not result:
        raise HTTPException(status_code=404, detail="Category or task not found")

    return result

@router.delete("/categories/{category_id}/tasks/{task_id}", response_model=TaskCategory, dependencies=[Depends(authenticate)])
async def delete_task_endpoint(category_id: str, task_id: str):
    print(category_id)
    print(task_id)
    result = await delete_task(category_id, task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Category or task not found")
    return result

@router.delete("/categories/{category_id}", dependencies=[Depends(authenticate)])
async def delete_category_endpoint(category_id: str):
    result = await delete_category(category_id)
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"} 