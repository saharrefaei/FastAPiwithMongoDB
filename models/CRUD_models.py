from datetime import datetime
from pydantic import BaseModel

class CRUD (BaseModel):
 name: str | None
 description : str | None
 creationDate : datetime | None 
 