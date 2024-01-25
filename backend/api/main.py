from fastapi import FastAPI,HTTPException,Depends,status
from pydantic import BaseModel
from typing import Annotated
import models
from db import engine, SessionLocal
from sqlalchemy.orm import Session
import auth
from auth import get_current_user

app=FastAPI()
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]

@app.get("/readElector/", status_code = status.HTTP_200_OK)
async def read_elector( ci: str, f_nac: str, db: db_dependency):
    elector = db.query(models.elector).filter(models.elector.ci_elector == ci, models.elector.fecha_nacimiento == f_nac).first()
    if elector is None:
        raise HTTPException(status_code=404, detail = 'elector no encontrado')
    return elector

@app.get("/loginAdmin/", status_code = status.HTTP_200_OK)
async def read_admin( username: str, password: str, db: db_dependency):
    admin = db.query(models.administrador).filter(models.administrador.username == username, models.administrador.contrasena == password).first()
    if admin is None:
        raise HTTPException(status_code=404, detail = 'admin no encontrado')
    return admin

@app.get("/loginComite/", status_code = status.HTTP_200_OK)
async def read_comite( ci: str, password: str, db: db_dependency):
    comite = db.query(models.comite_electoral).filter(models.comite_electoral.ci_Comite == ci, models.comite_electoral.contrasena == password).first()
    if comite is None:
        raise HTTPException(status_code=404, detail = 'usuario de comite electoral no encontrado')
    return comite

@app.get("/login",status_code=status.HTTP_200_OK)
async def elec(ci: user_dependency, db: db_dependency):
    if elec is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='autenticacion fallida')
    return {'elector':elec}