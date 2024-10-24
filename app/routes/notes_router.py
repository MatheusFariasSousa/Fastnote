from fastapi import Depends,APIRouter,status

from sqlalchemy.orm import Session

from app.use_case.notes_use_cases import Notes_Use_Case

from app.db.deps import get_conection
from app.db.model import Notes
from app.db.model import User   

from app.security.user import get_current_user

from app.schema.notes_schema import Note_Schema,Note_Schema_Output

note_router=APIRouter(prefix="/note",tags=["Notes"])


"""@note_router.post("/post")
def post_note(note:Note_Schema,db_session:Session= Depends(get_conection),user: User = Depends(get_current_user)):
    uc = Notes_Use_Case(db_session=db_session)
    uc.post_not(notes=note,user=user)
    return status.HTTP_200_OK"""
    




