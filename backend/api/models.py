from sqlalchemy import Table,Column,Integer,String,Date
from db import Base

class elector(Base):
    __tablename__= 'elector'

    ci_elector = Column(String(10), primary_key=True, index=True)
    nombre = Column(String(255))
    apellido_paterno = Column(String(255))
    apellido_materno = Column(String(255))
    fecha_nacimiento = Column(Date)
    estado = Column(String(255))

class administrador(Base):
    __tablename__='administrador'

    id_admin = Column(Integer,primary_key=True, index=True)
    username = Column(String(255))
    contrasena = Column(String(255))

class comite_electoral(Base):
    __tablename__= 'comite_electoral'

    id_comite = Column(Integer,primary_key=True,index=True)
    ci_Comite = Column(String(10))
    contrasena = Column(String(25))

    