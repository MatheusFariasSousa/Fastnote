from fastapi import APIRouter,Form,Depends,status,HTTPException,Response,Body
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from app.db.deps import get_conection
from app.db.model import Notes
from app.db.model import User   
from app.schema.user_schema import User_schema,User_Schema_Output
from app.schema.notes_schema import Note_Schema
from app.use_case.user_use_cases import User_use_cases
from app.use_case.notes_use_cases import Notes_Use_Case
from app.use_case.pdf_use_cases import Pdf_Use_Case
from app.use_case.email_use_cases import Emai_Use_Case
from app.security.user import create_access_token,get_current_user,decode_token,get_user_from_payload
from fastapi.responses import StreamingResponse,JSONResponse


from passlib.context import CryptContext

front_router = APIRouter(prefix="/front",tags=["Front"])

crypt =CryptContext(schemes=["sha256_crypt"])



templates = Jinja2Templates(directory="app/templates")


@front_router.get("/")
def read_front(request:Request):
        return templates.TemplateResponse(request=request,name="index.html")

@front_router.post("/result-form",response_model=User_Schema_Output)
def post_front(fname:str=Form(...),cpf:str= Form(...),password:str= Form(...),db_session:Session = Depends(get_conection)):
    person = User_schema(name=fname,cpf=cpf,password=password)
    uc = User_use_cases(db_session=db_session)
    uc.post_user(person)
    return RedirectResponse(url=f"/front", status_code=status.HTTP_303_SEE_OTHER)

@front_router.post("/get-token")
def get_token(response:Response,forms:OAuth2PasswordRequestForm = Depends(),db_session:Session = Depends(get_conection)):
    user = db_session.query(User).where(User.name==forms.username).first()
    if not user or not crypt.verify(forms.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Usuario ou senha incorreto")
    access_token = create_access_token(data={"sub":forms.username})
    if(user.name=="admin" and crypt.verify("admin",user.password)):
        return {"access_token": access_token,"token_type":"bearer","name":user.name}
    return {"access_token": access_token,"token_type":"bearer"}
    



@front_router.post("/notes")
def post_note(token:str=Form(...),title:str=Form(...),notetext:str=Form(...),db_session:Session = Depends(get_conection)):
    payload = decode_token(token=token)
    current_user = get_user_from_payload(db_session=db_session,payload=payload)
    notation = Note_Schema(title=title,text=notetext)
    uc= Notes_Use_Case(db_session=db_session)
    uc.post_not(notation,current_user)
    return RedirectResponse(url=f"/front/notes/{token}", status_code=status.HTTP_303_SEE_OTHER)

@front_router.get("/notes/{token}")
def read_notes(request:Request,token:str,db_session:Session = Depends(get_conection)):
    payload = decode_token(token=token)
    current_user = get_user_from_payload(db_session=db_session,payload=payload)
    notes = db_session.query(Notes).where(Notes.user_id==current_user.id)
    return templates.TemplateResponse("oi.html",{"request":request,"notes":notes,"user":current_user,"token": token})

@front_router.post("/delete-note/{id}")
def deleteNote(id:int,token:str=Form(...),db_session:Session = Depends(get_conection)):
    payload = decode_token(token=token)
    current_user = get_user_from_payload(db_session=db_session,payload=payload)
    uc = Notes_Use_Case(db_session=db_session)
    uc.delete_note(id = id,user=current_user)
    return RedirectResponse(url=f"/front/notes/{token}", status_code=status.HTTP_303_SEE_OTHER)

@front_router.post("/put-note/{id}")
def put_note(id:int,token:str=Form(...),title:str=Form(...),note:str=Form(...),db_session:Session = Depends(get_conection)):
         

        payload = decode_token(token=token)
        current_user = get_user_from_payload(db_session=db_session, payload=payload)
        uc = Notes_Use_Case(db_session=db_session)
        notes = Note_Schema(title=title, text=note)
        uc.put_note(id, notes=notes, user=current_user)

        return RedirectResponse(url=f"/front/notes/{token}", status_code=status.HTTP_303_SEE_OTHER)
    

@front_router.post("/download-pdf/{id}")
def download_pdf(id:int,db_session:Session = Depends(get_conection)):
    try:
        uc = Pdf_Use_Case(db_session=db_session, id=id)
        pdf_buffer = uc.create_pdf_in_memory()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    
    filename = f"{uc.title.replace(' ', '_')}.pdf"

    
    return StreamingResponse(pdf_buffer, media_type="application/pdf", headers={
        "Content-Disposition": f"attachment; filename={filename}"
    })




@front_router.get("/notes/list/{token}")
def read_notes_all(request:Request,token:str,db_session:Session = Depends(get_conection)):
    payload = decode_token(token=token)
    current_user = get_user_from_payload(db_session=db_session,payload=payload)
    notes = db_session.query(Notes).where(Notes.user_id==current_user.id)
    return templates.TemplateResponse("list.html",{"request":request,"notes":notes,"user":current_user,"token": token})

@front_router.post("/email")
def print_email(data:dict = Body(...),db_session:Session = Depends(get_conection)):
    uc = Emai_Use_Case(db_session=db_session)
    uc.enviar_email(id=int(data["id"]),email_user=data["email"])
    return status.HTTP_200_OK
     
@front_router.get("/userslist")
def teste_front(request:Request,db_session:Session = Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    users_list = uc.get_all()
    return  templates.TemplateResponse("crud.html",{"request":request,"users_list":users_list})
    
@front_router.delete("/deleteUser/{cpf}")
def deleteUser(request: Request,cpf:str,db_session:Session = Depends(get_conection)):
     uc = User_use_cases(db_session=db_session)
     uc.delete_user_by_cpf(cpf=cpf)
     users_list = uc.get_all()
     return  templates.TemplateResponse("crud.html",{"request":request,"users_list":users_list})

@front_router.get("/verNotasModal/{cpf}")
def verNotasModal(request: Request , cpf:str, db_session:Session = Depends(get_conection)):
    ucUser = User_use_cases(db_session=db_session)
    user_id = ucUser.getUserIdByCpf(cpf=cpf)
    print(user_id)
    uc = Notes_Use_Case(db_session=db_session)
    notesList = uc.openModal(user_id=user_id)
    print(notesList)
    notes_data = [
        {
            "title": note.title,
            "created_at": note.created_at.strftime('%d/%m/%Y %H:%M')
        }
        for note in notesList
    ]
    return JSONResponse(content={"notesList": notes_data})

@front_router.post("/abrirNota/{title}")
def abrirNotaModal(request:Request , title:str, db_session:Session = Depends(get_conection)):
    uc = Notes_Use_Case(db_session=db_session)
    return uc.getNoteByTitle(title=title)
    

    
    





    


    