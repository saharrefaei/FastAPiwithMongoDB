from fastapi import FastAPI
from routes.CRUD_routes import CRUDs_APPLICATION_ROUTER
app = FastAPI()

app.include_router(CRUDs_APPLICATION_ROUTER)
