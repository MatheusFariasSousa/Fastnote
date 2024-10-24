from pydantic import BaseModel
from datetime import datetime

class Note_Schema(BaseModel):
    title:str
    text:str

class Note_Schema_Output(Note_Schema):
    id:int
    created_at:datetime

    