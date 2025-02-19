from fastapi import APIRouter
from fastapi import  Request
from typing import Union
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")
@note.get("/", response_class=HTMLResponse)
async def read(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id" : doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"], 
            "important": doc["important"] 
        })
    return templates.TemplateResponse(
     name="index.html", context = {"request": request ,"newDocs": newDocs}
    )
    
@note.post("/")
async def get_note(request : Request):
    form = await request.form()
    print(form)
    formDict = dict(form)
    is_important = "important" in formDict
    # Make sure to add validation or default values if needed
    noteData = {
        "title": formDict.get("title", ""),
        "desc": formDict.get("desc", ""),
        "important": is_important
    }
    # Use the same collection path as in your GET route
    result = conn.notes.notes.insert_one(noteData)
    return {"success": True, "id": str(result.inserted_id)}