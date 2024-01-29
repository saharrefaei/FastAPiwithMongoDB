from fastapi import APIRouter
from config.database import collection_Name
from models.CRUD_models import CRUD
from schemas.CRUD_schemas import CRUD_serializer , CRUDs_serializer

from enum import Enum

CRUDs_APPLICATION_ROUTER = APIRouter()

 
@CRUDs_APPLICATION_ROUTER.get("/" , description='This is my first get api')
async def CRUD_API():
    CRUDs_APPLICATION = CRUDs_serializer(collection_Name.find()) 
    return {"status" : "ok"}
