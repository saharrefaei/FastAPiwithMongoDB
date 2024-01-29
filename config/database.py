from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://saharrefaei:Sahar657285@cluster.p5meqfs.mongodb.net/?retryWrites=true&w=majority")

db = client.CRUD_application

collection_Name = db["CRUD_app"]