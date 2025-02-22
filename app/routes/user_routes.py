from sqlalchemy.orm import Session
from fastapi import Depends,APIRouter,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.db.model import User
from app.db.deps import get_conection
from app.schema.user_schema import User_schema,User_Schema_Output
from app.schema.token_schema import Token
from app.use_case.user_use_cases import User_use_cases
from app.security.user import create_access_token,get_current_user
from passlib.context import CryptContext

router = APIRouter(prefix="/user",tags=["User"])
crypt =CryptContext(schemes=["sha256_crypt"])

@router.post("/post")
def post_user(user:User_schema,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    uc.post_user(user=user)
    return status.HTTP_200_OK

@router.get("/get/{id}",response_model=User_Schema_Output)
def get_by_id(id:int,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    person = uc.get_by_id(id=id)
    return person

@router.get("/get")
def get_all(db_session:Session = Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    return uc.get_all()

@router.delete("/delete/{id}")
def delete(id:int,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    return uc.delete_user(id=id)

@router.put("/put/{id}",response_model=User_Schema_Output)
def put(id:int,user:User_schema,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    return uc.put_user(id=id,user=user)

@router.post("/token",response_model=Token,tags=["Token"])
def user_token(forms:OAuth2PasswordRequestForm = Depends(),db_session:Session=Depends(get_conection)):
    user = db_session.query(User).where(User.name==forms.username).first()
    if not user or not crypt.verify(forms.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Usuario ou senha incorreto")
    access_token = create_access_token(data={"sub":user.name})

    return {"access_token": access_token,"token_type":"bearer"}


@router.get("/get_you")
def get_you(db_session:Session=Depends(get_conection),current_user:User = Depends(get_current_user)):
    person = db_session.query(User).where(User.name==current_user.name).first()
    return person


