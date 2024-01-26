from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from db import SessionLocal
from models import elector,administrador,comite_electoral
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY='67fedca391aeae0238f112432ffacc1e8bd11d10e6471ca999186758175f2c90'
ALGORITHM= 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class CreateLoginRequest(BaseModel):
    ci: str
    f_nac: str

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/token", response_model=Token)
async def login_for_access_token(ci: str , fecha_nac: str , db: db_dependency):
    elec = authenticate_elector(ci, fecha_nac, db)
    if not elec:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='no es un elector valido')
    token = create_access_token(elec.nombre, elec.ci_elector, timedelta(minutes=5))

    return {'access_token': token, 'token_type': 'bearer'}


def authenticate_elector(username: str, password: str, db):
    elec = db.query(elector).filter(elector.ci_elector == username).first()
    pass_elec = elec.fecha_nacimiento.strftime('%Y-%m-%d')
    hashed_pass = bcrypt_context.hash(pass_elec) 
    if not elec:
        return False
    if not bcrypt_context.verify(password, hashed_pass):
        return False
    return elec

def create_access_token(username: str, userid: str, expires_delta: timedelta):
    encode = {'nombre':username,'ci_elector':userid}
    expires = datetime.utcnow()+ expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        nombre: str = payload.get('nombre')
        ci_elector: str = payload.get('ci_elector')
        if nombre is None or ci_elector is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user')
        return {'nombre': nombre,'ci':ci_elector}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='could not validated user')
