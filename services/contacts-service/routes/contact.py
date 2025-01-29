from fastapi import APIRouter, HTTPException, status
from models.contact import ContactRequest
from app.core.db import contact_collection
from bson import ObjectId

router = APIRouter()

# POST /contact-requests/
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_contact_request(contact_request: ContactRequest):
    contact_data = contact_request.dict()
    result = await contact_collection.insert_one(contact_data)
    return {"id": str(result.inserted_id), "message": "Contact request submitted successfully."}

# GET /contact-requests/
@router.get("/")
async def get_all_contact_requests():
    contacts = await contact_collection.find().to_list(100)
    return [{"id": str(contact["_id"]), **contact} for contact in contacts]

# GET /contact-requests/{user_id}
@router.get("/{user_id}")
async def get_contact_requests_by_user_id(user_id: str):
    contacts = await contact_collection.find({"email": user_id}).to_list(100)
    return [{"id": str(contact["_id"]), **contact} for contact in contacts]

# DELETE /contact-requests/{id}
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact_request(id: str):
    result = await contact_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact request not found")
    return {"message": "Contact request deleted successfully."}
