from sqlalchemy import Table,Column,Integer,String,Date
from db import Base

class elector(Base):
    __tablename__= 'elector'

    ci_elector = Column(String(10), primary_key=True, index=True, null=False)
    nombre = Column(String(255))
    apellido_paterno = Column(String(255))
    apellido_materno = Column(String(255))
    fecha_nacimiento = Column(Date)
    estado = Column(String(255))

    