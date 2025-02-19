def noteEntity(items) -> dict:
    return{
        "id" : str(items["_id"]),
        "title" : items["title"],
        "desc" : items["desc"],
        "important" : items["important"],    
    }
    
def notesEntity(items) -> list:
    return [noteEntity(items) for item in items]