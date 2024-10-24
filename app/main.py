from fastapi import FastAPI
from app.routes.user_routes import router
from app.routes.front_form_router import front_router
from app.routes.notes_router import note_router
from fastapi.staticfiles import StaticFiles



app = FastAPI()



@app.get("/")
def get_user():
    return "teste"

app.include_router(router=router)
app.include_router(router=front_router)
app.include_router(router=note_router)

app.mount("/app/static",StaticFiles(directory="app/static"),name="static")

