from fastapi import FastAPI , Query , Path
from enum import Enum

app = FastAPI()

 
@app.get("/" , description='This is my first get api')
async def root():
    return {"hi , you are in the root get / "}
