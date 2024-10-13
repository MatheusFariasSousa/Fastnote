from pydantic import BaseModel

class User_schema(BaseModel):
    name:str
    cpf:str
    password:str

class User_Schema_Output(BaseModel):
    name:str
    cpf:str



