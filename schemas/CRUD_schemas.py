def CRUD_serializer(CRUD) -> dict :
    return{
        "id" : str(CRUD["_id"]),
        "name" : CRUD["name"],
        "description" : CRUD["description"],
        "creationDate": CRUD["creationDate"]

    }
    
    
def CRUDs_serializer (CRUDs) -> list :
    return [ CRUD_serializer(CRUD) for CRUD in CRUDs ]