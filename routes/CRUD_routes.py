from fastapi import APIRouter
from config.database import collection_Name
from models.CRUD_models import CRUD
from schemas.CRUD_schemas import CRUD_serializer , CRUDs_serializer
from bson import ObjectId
from enum import Enum

CRUDs_APPLICATION_ROUTER = APIRouter()

 
@CRUDs_APPLICATION_ROUTER.get("/" , description='This is my first get api')
async def GET_CRUD_API():
    CRUDs_APPLICATION = CRUDs_serializer(collection_Name.find()) 
    return {"status" : "ok" , "data":CRUDs_APPLICATION}


@CRUDs_APPLICATION_ROUTER.get("/{id}" , description='This is get with id api')
async def GET_CRUD_API(id : str):
    CRUD_APPLICATION = CRUDs_serializer(collection_Name.find({"_id": ObjectId(id)})) 
    return {"status" : "ok" , "data":CRUD_APPLICATION}

@CRUDs_APPLICATION_ROUTER.post("/" , description='This is my first post api')
async def POST_CRUD_API(CRUD : CRUD):
    _id = collection_Name.insert_one(dict(CRUD))
    return CRUDs_serializer(collection_Name.find({"_id": _id.inserted_id}))


@CRUDs_APPLICATION_ROUTER.put("/{id}")
async def update_todo(id: str, todo: CRUD):
    collection_Name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(todo)
    })
    return CRUDs_serializer(collection_Name.find({"_id": ObjectId(id)}))

@CRUDs_APPLICATION_ROUTER.delete("/{id}")
async def delete_todo(id: str):
    collection_Name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}