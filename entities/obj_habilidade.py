from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Habilidade(DeclarativeBase):
    id_hab = Column(Integer, primary_key=True)
    hab_nome = Column(String(200), nullable=False)