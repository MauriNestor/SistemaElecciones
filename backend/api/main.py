from fastapi import FastAPI,HTTPException,Depends,status
from pydantic import BaseModel
from typing import Annotated
import models
from db import engine, SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

class getElector(BaseModel):
    ci: str
    nombre: str
    ap_p: str
    ap_m: str
    f_nac: str
    estado: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/login/{nombre}", status_code = status.HTTP_200_OK)
async def read_elector( ci: str, db: db_dependency):
    elector = db.query(models.elector).filter(models.elector.ci_elector == ci).first()
    if elector is None:
        raise HTTPException(status_code=404, detail = 'elector no encontrado')
    return elector